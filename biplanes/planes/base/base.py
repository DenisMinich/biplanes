"""BasePlane implementation"""

from kivy.properties import BooleanProperty
from kivy.properties import ListProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.vector import Vector

from biplanes.base_entity import BaseEntity


# pylint: disable=too-many-instance-attributes
class BasePlane(BaseEntity):
    """Common entity for all planes"""

    max_velocity = NumericProperty()
    """Maximal velocity for a plane"""

    max_points = NumericProperty()
    """Maximal hit points of plane"""

    team = ObjectProperty()
    """String with team identifier"""

    points = NumericProperty()
    """Hit points of plane"""

    is_in_air = BooleanProperty(False)
    """Flag, specified if plane in fly"""

    is_in_move = BooleanProperty()
    """Flag, specified if plane has started movement"""

    texture = ObjectProperty()
    """Image representation of plane"""

    velocity = NumericProperty()
    """Actual velocity"""

    tags = ListProperty(["plane"])

    @property
    def velocity_vector(self):
        """Vector of plane's velocity"""
        engine_velocity_vector = Vector(self.velocity, 0).rotate(self.angle)
        if self.is_in_air:
            gravity_velocity_vector = (
                Vector(0, -1) * (self.max_velocity - self.velocity))
        else:
            gravity_velocity_vector = Vector(0, 0)
        return engine_velocity_vector + gravity_velocity_vector

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

    angle = NumericProperty(0)
    """Rotation angle"""

    is_contains_pilot = BooleanProperty(True)
    """Is pilot inside of the plane"""

    DEATH_DAMAGED = 'damaged'
    """Death cause for plane got too much damage"""

    DEATH_CRASH = 'crash'
    """Death cause for plane crashed with decoration"""

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

    def __init__(self, *args, **kwargs):
        super(BasePlane, self).__init__(*args, **kwargs)
        self.register_event_type('on_destroy')

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
        return self.gun.fire()

    def damage(self, amount):
        """Decrease points value by amount"""
        self.points = 0 if amount >= self.points else self.points - amount
        if not self.points:
            self.destroy(self.DEATH_DAMAGED)

    def destroy(self, cause):
        """Decrease health points to zero"""
        self.dispatch('on_destroy', cause)
        self.remove_item(self)

    def on_destroy(self, cause):
        """Method should be called if plane was destroyed"""
        pass

    def update(self):
        """Update state of the plane"""
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
            if self.velocity == self.max_velocity:
                self.is_in_air = True
