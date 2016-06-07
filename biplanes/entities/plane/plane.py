import os

from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.properties import BoundedNumericProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.vector import Vector
from parabox.behaviour import Collidable
from parabox.behaviour import Movable
from parabox.phisics import PlainPhisics
from parabox.structures import Collector
from parabox.structures import ObjectsCollection

from biplanes.entities.bullet.bullet import Bullet
from biplanes.entities.plane.plane_states import PlaneStates
from biplanes.entities.plane import settings as plane_settings
from biplanes.entities.state_machine.state_machine import StateMachine
from biplanes import settings as global_settings


class Plane(Movable, StateMachine, Collidable):
    """Common entity for all planes"""

    points = BoundedNumericProperty(3, max=3, min=0)
    """Hit points of plane"""

    in_air = BooleanProperty(False)
    """Flag, specified if plane if fly"""

    team = StringProperty()
    """String with team identifier"""

    texture = ObjectProperty()
    """Image representation of plane"""

    fixed_velocity = BoundedNumericProperty(
        0, min=0, max=plane_settings.MAX_SPEED_X,
        errorhandler=lambda x: 0 if x < 0 else plane_settings.MAX_SPEED_X)
    """Self velocity (engine analog)"""

    _controller = None
    """Controller of a plane"""

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, value):
        if self._controller is not None:
            self._controller.unassign()
        self._controller = value
        self._controller.assign(self)

    def __init__(self, *args, **kwargs):
        super(Plane, self).__init__(
            resistance_y=.05,
            speed_limit_x=plane_settings.MAX_SPEED_X,
            speed_limit_y=plane_settings.MAX_SPEED_Y,
            *args, **kwargs)
        self.lift = PlainPhisics(affect_objects=[self])
        self.inner_phisics = ObjectsCollection([self.lift], self)

    def increase_velocity(self, *args):
        self.fixed_velocity += .03

    def decrease_velocity(self, *args):
        self.fixed_velocity -= .03

    def fire(self):
        return Bullet(owner=self)

    def damage(self, amount):
        self.points = 0 if amount >= self.points else self.points - amount

    def destroy(self):
        self.points = 0

    def _process_collissions(self, instance, collide_object):
        if (collide_object in Collector.get_collection('environment') and
                collide_object in Collector.get_collection('solid')):
            self.destroy()

    def _apply_arteficial_velocity(self, *args):
        self.move_manual(*self._get_fixed_velocity_vector())

    def _check_takeoff_point(self, *args):
        if self.fixed_velocity > plane_settings.TAKEOFF_POINT:
            self.in_air = True

    def _update_lift(self, *args):
        if self.in_air:
            if self.fixed_velocity >= plane_settings.TAKEOFF_POINT:
                lift_value = global_settings.GLOBAL_GRAVITY
            else:
                diff = plane_settings.TAKEOFF_POINT - self.fixed_velocity
                if diff > plane_settings.POWER_DOWNGRADE_RANGE:
                    lift_value = 0
                else:
                    lift_value = ((plane_settings.POWER_DOWNGRADE_RANGE -
                                   diff) * global_settings.GLOBAL_GRAVITY)
            self.lift.gravity = Vector(0, lift_value)

    def _return_to_scene(self, *args, **kwargs):
        if self.x + self.size[0] > self.parent.size[0]:
            self.pos[0] = 0
        if self.x < 0:
            self.pos[0] = self.parent.size[0] - self.size[0]
        if self.y + self.size[1] > self.parent.size[1]:
            self.pos[1] = 0
        if self.y < 0:
            self.pos[1] = self.parent.size[1] - self.size[1]

    def _get_fixed_velocity_vector(self):
        return Vector(self.fixed_velocity, 0).rotate(self.angle)

    @staticmethod
    def on_points(self, value):
        if value == 3:
            self.change_state(PlaneStates.STATE_NORMAL)
        elif value == 2:
            self.change_state(PlaneStates.STATE_DAMAGED)
        elif value == 1:
            self.change_state(PlaneStates.STATE_CRITICAL_DAMAGED)
        elif value == 0:
            self.change_state(PlaneStates.STATE_BANG)

    def __repr__(self):
        return "<Plane id='%s'>" % self.id
