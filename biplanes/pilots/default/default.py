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
        if self.is_in_air:
            initial_velocity_vector = (
                vector.Vector(1, 0).rotate(self.angle) * self.velocity)
            gravity_velocity_vector = (
                vector.Vector(0, -1) * self.gravity_velocity)
            return initial_velocity_vector + gravity_velocity_vector
        else:
            left_run_velocity = self.is_run_left * self.running_velocity
            right_run_velocity = self.is_run_right * self.running_velocity
            return vector.Vector(right_run_velocity - left_run_velocity, 0)

    def __init__(self, *args, **kwargs):
        self._texture = Image(source='pilot.png').texture
        self.is_in_air = True
        self.gravity = .07
        self.gravity_velocity = 0
        self.gravity_max_velocity = 15
        self.is_run_left = False
        self.is_run_right = False
        self.running_velocity = 1
        self.velocity = 0
        self.velocity_resistance = .05
        super(DefaultPilot, self).__init__(*args, **kwargs)
        self.register_event_type('on_landed')
        self.register_event_type('on_reach_spawn')

    def on_landed(self):
        """Called if case pilot successfullt langed"""
        pass

    def on_reach_spawn(self):
        """Called if case pilot successfullt reached planes' spawn"""
        pass

    def update(self):
        self._update_initial_velocity()
        self._update_gravity_velocity()
        self._move()

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

    def on_destroy(self, cause):
        """Method should be called if plane was destroyed"""
        pass

    def collide(self, item):
        if item.has_tags('ground'):
            self.is_in_air = False
            self._correct_landed_position(item)
            self.dispatch('on_landed')
        if item.has_tags('spawn'):
            if not self.is_in_air:
                self.dispatch('on_reach_spawn')

    def _correct_landed_position(self, ground):
        """Move pilot to the ground top

        After pilot falling, he can stuck in ground texture if he had high
        velocity, so we move him a bit to the top of the ground
        """
        while self.collide_widget(ground):
            self.center_y += 1
