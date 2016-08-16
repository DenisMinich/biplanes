"""BasePlane implementation"""

from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.vector import Vector
from parabox.behaviour import Collidable
from parabox.behaviour import Movable

from biplanes.entities.state_machine.state_machine import StateMachine


# pylint: disable=too-many-ancestors
class BasePlane(Collidable, Movable, StateMachine):
    """Common entity for all planes"""

    takeoff_point = NumericProperty()
    """Minimal speed to takeoff"""

    max_velocity = NumericProperty()
    """Maximal velocity for a plane"""

    max_points = NumericProperty()
    """Maximal hit points of plane"""

    team = StringProperty()
    """String with team identifier"""

    points = NumericProperty()
    """Hit points of plane"""

    in_air = BooleanProperty()
    """Flag, specified if plane in fly"""

    in_move = BooleanProperty()
    """Flag, specified if plane has started movement"""

    texture = ObjectProperty()
    """Image representation of plane"""

    velocity = NumericProperty()
    """Actual velocity"""

    @property
    def velocity_vector(self):
        """Vector of plane's velocity"""
        return Vector(self.velocity, 0).rotate(self.angle)

    acceleration = NumericProperty()
    """How quick plane picks up velocity"""

    braking = NumericProperty()
    """How quick plane loses velocity"""

    rotate_clockwise_velocity = NumericProperty()
    """Velocity of clockwise rotation"""

    rotate_conterclockwise_velocity = NumericProperty()
    """Velocity of clockwise rotation"""

    scene = ObjectProperty()
    """Scene object"""

    gun = ObjectProperty()
    """Gun object"""

    @property
    def control(self):
        """Property for control"""
        return self._control

    @control.setter
    def control(self, value):
        if self._control is not None:
            self._control.unassign()
        self._control = value
        self._control.assign(self)

    _control = ObjectProperty()
    """Control of a plane"""

    def increase_velocity(self, *_):
        """Increase plane's velocity by acceleration value"""
        self.velocity += self.acceleration

    def decrease_velocity(self, *_):
        """Decrease plane's velocity by braking value"""
        self.velocity -= self.braking

    def rotate_clockwise(self, *_):
        """Rotate planes direction clockwise"""
        self.angle -= self.rotate_clockwise_velocity

    def rotate_conterclockwise(self, *_):
        """Rotate planes direction conterclockwise"""
        self.angle += self.rotate_conterclockwise_velocity

    def fire(self):
        """Spawn bullet"""
        return self.gun.fire(
            pos=self.pos,
            size=self.size,
            angle=self.angle)

    def damage(self, amount):
        """Decrease points value by amount"""
        self.points = 0 if amount >= self.points else self.points - amount

    def destroy(self):
        """Decrease health points to zero"""
        self.points = 0

    def _process_collissions(self, *_):
        for scene_objects in self.scene.environment:
            if scene_objects.is_solid:
                self.destroy()

    def _check_takeoff_point(self, *_):
        if self.velocity > self.takeoff_point:
            self.in_air = True

    def _return_to_scene(self, *_):
        plane_length = self.size[0]
        scene_length = self.scene.size[0]
        if self.center_x > scene_length:
            self.pos[0] = -plane_length / 2
        if self.center_x < 0:
            self.pos[0] = scene_length - plane_length / 2
