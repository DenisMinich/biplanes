from functools import partial

from kivy.logger import Logger
from kivy.properties import BooleanProperty
from kivy.properties import BoundedNumericProperty
from kivy.properties import NumericProperty
from kivy.vector import Vector
from kivy.uix.image import Image
from parabox.behaviour import Collidable
from parabox.behaviour import Movable
from parabox.phisics import PlainPhisics
from parabox.structures import ObjectsCollection

from biplanes import settings as global_settings
from biplanes.entities.bullet.bullet import Bullet
from biplanes.entities.plane import settings as plane_settings


class Plane(Movable, Image, Collidable):

    STATE_ON_START = 1
    STATE_NORMAL = 2
    STATE_DAMAGED = 3
    STATE_CRITICAL_DAMAGED = 4
    STATE_NO_PILOT = 5
    STATE_BANG = 6

    state = NumericProperty(STATE_ON_START)
    points = BoundedNumericProperty(3, max=3, min=0)
    in_air = BooleanProperty(False)
    fixed_velocity = BoundedNumericProperty(
        0, min=0, max=plane_settings.MAX_SPEED_X,
        errorhandler=lambda x: 0 if x < 0 else plane_settings.MAX_SPEED_X)

    def __init__(self, *args, **kwargs):
        super(Plane, self).__init__(
            resistance_y=.05,
            speed_limit_x=plane_settings.MAX_SPEED_X,
            speed_limit_y=plane_settings.MAX_SPEED_Y,
            *args, **kwargs)
        self.lift = PlainPhisics(affect_objects=[self])
        self.inner_phisics = ObjectsCollection([self.lift], self)
        self.anim_delay = -.1
        self.anim_loop = 1
        self.start = partial(self._initialize, *args, **kwargs)
        self.start()

    def increase_velocity(self, *args):
        self.fixed_velocity += .03

    def decrease_velocity(self, *args):
        self.fixed_velocity -= .03

    def fire(self):
        return Bullet(owner=self)

    def damage(self, amount):
        self.points -= amount

    def _initialize(self, *args, **kwargs):
        self.delete_from_collections(['hidden_objects'])
        self.add_to_collections(['planes', 'game_objects'])
        self.bind(on_update=self._apply_arteficial_velocity)
        self.bind(on_update=self._return_to_scene)
        self.bind(fixed_velocity=self._check_takeoff_point)
        self.bind(fixed_velocity=self._update_lift)
        self.lift.gravity = Vector(0, global_settings.GLOBAL_GRAVITY)
        self.pos = kwargs.get('start_pos')
        self.size = (35, 35)
        self.in_air = False
        self.state = self.STATE_ON_START
        self.points = 3
        self.fixed_velocity = 0

    def hide(self):
        self.delete_from_collections(['game_objects'])
        self.add_to_collections(['hidden_objects'])
        self.unbind(on_update=self._apply_arteficial_velocity)
        self.unbind(on_update=self._return_to_scene)
        self.unbind(fixed_velocity=self._check_takeoff_point)
        self.unbind(fixed_velocity=self._update_lift)
        self.size = (0, 0)

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
                lift_value = (
                    0 if diff > plane_settings.POWER_DOWNGRADE_RANGE
                    else (plane_settings.POWER_DOWNGRADE_RANGE - diff) * global_settings.GLOBAL_GRAVITY)
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
            self.state = self.STATE_NORMAL
        elif value == 2:
            self.state = self.STATE_DAMAGED
        elif value == 1:
            self.state = self.STATE_CRITICAL_DAMAGED
        elif value == 0:
            self.state = self.STATE_BANG

    @staticmethod
    def on_state(self, value):
        if self.state == self.STATE_ON_START:
            self.source = 'red_plane.png'
        if self.state == self.STATE_NORMAL:
            self.source = 'red_plane.png'
        if self.state == self.STATE_DAMAGED:
            self.source = 'red_plane.png'
        if self.state == self.STATE_CRITICAL_DAMAGED:
            self.source = 'red_plane.png'
        if self.state == self.STATE_NO_PILOT:
            self.source = 'red_plane.png'
        if self.state == self.STATE_BANG:
            self.delete_from_collections(['planes'])
            self.lift.gravity = Vector(0, 0)
            self.move_stop()
            self.pos = (self.center_x - 32, self.center_y - 32)
            self.size = (64, 64)
            self.source = 'bang.gif'
            self.plan_action(30, self.hide)
            self.plan_action(90, self.start)

    def __repr__(self):
        return "<Plane id='%s'>" % self.id
