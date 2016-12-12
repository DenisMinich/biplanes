"""DefaultPilot implementation"""

from biplanes.mechanic.movable import movable

from kivy import properties
from kivy.uix.image import Image
from kivy import vector


# pylint: disable=too-many-ancestors
# pylint: disable=too-many-instance-attributes
class DefaultPilot(movable.Movable):
    """Base pilot widget"""

    texture = properties.ObjectProperty(None, allownone=True)
    """Widgets texture"""

    control = properties.ObjectProperty(None, allownone=True)
    """Control of a plane"""

    parachute = properties.ObjectProperty(None, allownone=True)
    """Parachute object"""

    is_landed = properties.BooleanProperty(False)
    """Is pilot on the ground"""

    is_run_left = properties.BooleanProperty(False)
    """Is pilot running left"""

    is_run_right = properties.BooleanProperty(False)
    """Is pilot running left"""

    initial_velocity = properties.ObjectProperty(vector.Vector(0, 0))
    """Velocity of catapultion. Reduced with time"""

    gravity_velocity = properties.ObjectProperty(vector.Vector(0, 0))
    """Velocity under gravity influence"""

    def get_run_velocity(self):
        """Calculate velocity of running"""
        result = vector.Vector(0, 0)
        if self.is_run_left:
            result += vector.Vector(-self.running_velocity, 0)
        if self.is_run_right:
            result += vector.Vector(self.running_velocity, 0)
        return result

    side_move_velocity = properties.AliasProperty(get_run_velocity)
    """Running velocity vector"""

    def get_velocity(self):
        """Vector of plane's velocity"""
        if self.is_landed:
            return self.side_move_velocity
        else:
            return self.initial_velocity + self.gravity_velocity

    velocity = properties.AliasProperty(get_velocity, bind=[
        'is_landed', 'side_move_velocity',
        'initial_velocity', 'gravity_velocity'])
    """Running velocity vector"""

    def __init__(self, *args, **kwargs):
        self.texture = Image(source='pilot.png').texture
        self.gravity = vector.Vector(0, -.05)
        self.max_gravity_velocity = 15
        self.running_velocity = 1
        self.velocity_resistance = .07
        self.initial_velocity = vector.Vector(0, 0)
        self.gravity_velocity = vector.Vector(0, 0)
        super(DefaultPilot, self).__init__(*args, **kwargs)
        self.register_event_type('on_landed')
        self.register_event_type('on_reach_spawn')

    def on_landed(self):
        """Called if case pilot successfullt langed"""
        self.is_landed = True

    def on_reach_spawn(self):
        """Called if case pilot successfullt reached planes' spawn"""
        pass

    def assign_control(self, value):
        """Proper way to assign control for widget"""
        self.unassign_control()
        self.control = value
        self.control.assign(self)

    def unassign_control(self):
        """Proper way to remove control from widget"""
        if self.control is not None:
            self.control.unassign()

    def update(self):
        self.update_initial_velocity()
        self.update_gravity_velocity()
        self.move()

    def update_initial_velocity(self):
        """Reduces velocity of catapultion with time"""
        absolute_initial_velocity = self.initial_velocity.length()
        if absolute_initial_velocity > 0:
            breaking = self.initial_velocity.rotate(
                180).normalize() * self.velocity_resistance
            absolute_breaking = breaking.length()
            if absolute_breaking > absolute_initial_velocity:
                self.initial_velocity = vector.Vector(0, 0)
            else:
                self.initial_velocity += breaking

    def update_gravity_velocity(self):
        """Increase gravity velocity to maximum value"""
        absolute_gravity_velocity = self.gravity_velocity.length()
        if absolute_gravity_velocity != self.max_gravity_velocity:
            if absolute_gravity_velocity < self.max_gravity_velocity:
                self.gravity_velocity += self.gravity
                absolute_gravity_velocity = self.gravity_velocity.length()
                if absolute_gravity_velocity > self.max_gravity_velocity:
                    self.gravity_velocity *= (
                        self.max_gravity_velocity / absolute_gravity_velocity)
            else:
                self.gravity_velocity += vector.Vector(
                    0, self.velocity_resistance)
                absolute_gravity_velocity = self.gravity_velocity.length()
                if absolute_gravity_velocity < self.max_gravity_velocity:
                    self.gravity_velocity *= (
                        absolute_gravity_velocity / self.max_gravity_velocity)

    def collide(self, item):
        if item.has_tags('ground'):
            self.correct_landed_position(item)
            self.dispatch('on_landed')
        if item.has_tags('spawn') and self.is_landed:
            self.dispatch('on_reach_spawn')

    def correct_landed_position(self, ground):
        """Move pilot to the ground top

        After pilot falling, he can stuck in ground texture if he had high
        velocity, so we move him a bit to the top of the ground
        """
        while self.collide_widget(ground):
            self.center_y += 1
