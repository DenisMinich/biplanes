"""DefaultPilot implementation"""

from biplanes.mechanic.movable import movable

from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy import vector


# pylint: disable=too-few-public-methods
# pylint: disable=too-many-ancestors
class DefaultPilot(movable.Movable):
    """Base pilot widget"""

    _texture = ObjectProperty()

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

    @property
    def velocity_vector(self):
        """Vector of plane's velocity"""
        initial_velocity_vector = (
            vector.Vector(1, 0).rotate(self.angle) * self.velocity)
        gravity_velocity_vector = (
            vector.Vector(0, -1) * self.gravity_velocity)
        return initial_velocity_vector + gravity_velocity_vector

    def __init__(self, *args, **kwargs):
        self._texture = Image(source='pilot.png').texture
        self.gravity = .07
        self.gravity_velocity = 0
        self.gravity_max_velocity = 15
        self.velocity = 0
        self.velocity_resistance = .05
        super(DefaultPilot, self).__init__(*args, **kwargs)

    def update(self):
        self.move()
        self._update_initial_velocity()
        self._update_gravity_velocity()

    def _update_initial_velocity(self):
        if self.velocity > 0:
            if self.velocity_resistance > self.velocity:
                self.velocity = 0
            else:
                self.velocity -= self.velocity_resistance

    def _update_gravity_velocity(self):
        if self.gravity_velocity != self.gravity_max_velocity:
            self.gravity_velocity += self.gravity
            if self.gravity_velocity > self.gravity_max_velocity:
                self.gravity_velocity = self.gravity_max_velocity
