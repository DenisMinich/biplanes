from kivy.properties import BooleanProperty
from kivy.properties import BoundedNumericProperty
from kivy.vector import Vector
from parabox.behaviour import Movable
from parabox.phisics import PlainPhisics
from parabox.structures import ObjectsCollection
from parabox.visual import ImageView

from biplanes.settings import GLOBAL_GRAVITY
from biplanes.settings import MAX_SPEED_X
from biplanes.settings import MAX_SPEED_Y
from biplanes.settings import POWER_DOWNGRADE_RANGE
from biplanes.settings import TAKEOFF_POINT
from biplanes.entities.bullet.bullet import Bullet


class Plane(Movable, ImageView):

    in_air = BooleanProperty(False)
    fixed_velocity = BoundedNumericProperty(
        0, min=0, max=MAX_SPEED_X,
        errorhandler=lambda x: 0 if x < 0 else MAX_SPEED_X)

    def __init__(self, *args, **kwargs):
        super(Plane, self).__init__(
            resistance_y=.05,
            speed_limit_x=MAX_SPEED_X, speed_limit_y=MAX_SPEED_Y,
            size=(35, 35), *args, **kwargs)
        self.add_to_collections(['planes'])
        self.lift = PlainPhisics(
            gravity=(0, GLOBAL_GRAVITY), affect_objects=[self])
        self.inner_phisics = ObjectsCollection([self.lift], self)
        self.bind(on_update=self._apply_arteficial_velocity)
        self.bind(on_update=self._return_to_scene)
        self.bind(fixed_velocity=self._check_takeoff_point)
        self.bind(fixed_velocity=self._update_lift)

    def increase_velocity(self, *args):
        self.fixed_velocity += .03

    def decrease_velocity(self, *args):
        self.fixed_velocity -= .03

    def _apply_arteficial_velocity(self, *args):
        self.move_manual(*self._get_fixed_velocity_vector())

    def _check_takeoff_point(self, *args):
        if self.fixed_velocity > TAKEOFF_POINT:
            self.in_air = True

    def _update_lift(self, *args):
        if self.in_air:
            if self.fixed_velocity >= TAKEOFF_POINT:
                lift_value = GLOBAL_GRAVITY
            else:
                diff = TAKEOFF_POINT - self.fixed_velocity
                lift_value = (
                    0 if diff > POWER_DOWNGRADE_RANGE
                    else (POWER_DOWNGRADE_RANGE - diff) * GLOBAL_GRAVITY)
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

    def fire(self):
        return Bullet(owner=self)
