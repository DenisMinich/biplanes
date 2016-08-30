"""BasePlane implementation"""

from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.vector import Vector
from parabox.behaviour import Collidable


# pylint: disable=too-many-ancestors
class BasePlane(Collidable):
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

    is_in_air = BooleanProperty()
    """Flag, specified if plane in fly"""

    is_in_move = BooleanProperty()
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

    def increase_velocity(self):
        """Increase plane's velocity by acceleration value"""
        if self.velocity != self.max_velocity:
            self.velocity += self.acceleration
            if self.velocity > self.max_velocity:
                self.velocity = self.max_velocity

    def decrease_velocity(self):
        """Decrease plane's velocity by braking value"""
        self.velocity -= self.braking

    def rotate_clockwise(self):
        """Rotate planes direction clockwise"""
        self.angle -= self.rotate_clockwise_velocity

    def rotate_conterclockwise(self):
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

    def update(self):
        self._check_is_in_move()
        self._check_is_in_air()
        self._move()

    def _move(self):
        self.pos = (
            self.pos[0] + self.velocity_vector[0],
            self.pos[1] + self.velocity_vector[1])

    def _check_is_in_move(self):
        if not self.is_in_move:
            if self.velocity:
                self.is_in_move = True

    def _check_is_in_air(self):
        if not self.is_in_air:
            if self.velocity > self.takeoff_point:
                self.is_in_air = True
