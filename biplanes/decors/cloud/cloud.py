"""Cloud implementation"""

from random import random

from kivy import properties
from kivy.uix.image import Image
from kivy.vector import Vector

from biplanes.base_entity import BaseEntity


# pylint: disable=too-many-instance-attributes
class Cloud(BaseEntity):
    """Cloud decoration"""

    texture = properties.ObjectProperty()
    """Self texture"""

    angle = properties.NumericProperty()
    """Rotation angle"""

    velocity = properties.NumericProperty()
    """Actual velocity"""

    velocity_middle = properties.NumericProperty()
    """Medium velocity"""

    velocity_dispersion = properties.NumericProperty()
    """How much velocity may diff from middle"""

    flight_height = properties.NumericProperty()
    """Actual flight height"""

    flight_height_middle = properties.NumericProperty()
    """Center of flight height corridor"""

    flight_height_dispersion = properties.NumericProperty()
    """How much flight height may change"""

    @property
    def velocity_vector(self):
        """Vector of velocity"""
        return Vector(self.velocity, 0).rotate(self.angle)

    def __init__(
            self, *args, angle=0, velocity_middle=0.4,
            velocity_dispersion=0.2, flight_height_middle=50,
            flight_height_dispersion=50, left_border=0, right_border=0,
            on_border_exceeded='circle', **kwargs):
        self.texture = Image(source='cloud.png').texture
        self.angle = angle
        self.velocity_middle = velocity_middle
        self.velocity_dispersion = velocity_dispersion
        self.flight_height_middle = flight_height_middle
        self.flight_height_dispersion = flight_height_dispersion
        self.left_border = left_border
        self.right_border = right_border
        self.top_border = None
        self.bottom_border = None
        self.on_border_exceeded = on_border_exceeded
        super(Cloud, self).__init__(*args, **kwargs)
        self.register_event_type('on_border')
        self.bind(on_border=self._renew_traits)
        self._setup_start_state()

    def on_border(self, *args, **kwargs):
        """Default handler for 'on_border' event"""
        pass

    def update(self):
        self._move()
        self._check_borders()

    def _move(self):
        self.pos = (
            self.pos[0] + self.velocity_vector[0],
            self.pos[1] + self.velocity_vector[1])

    def _check_borders(self):
        if self.on_border_exceeded == 'circle':
            borders_specified_not_in_pairs = (
                (self.right_border is None and self.left_border is not None) or
                (self.right_border is not None and self.left_border is None) or
                (self.top_border is None and self.bottom_border is not None) or
                (self.top_border is not None and self.bottom_border is None))
            if borders_specified_not_in_pairs:
                raise ValueError(
                    "If 'circle' border mechanic selected, borders should be "
                    "implemented in pairs: left/right or top/bottom.")
            if self.right_border is not None and self.left_border is not None:
                if self.center_x > self.right_border:
                    self.dispatch(
                        'on_border', 'right', self.center_x, self.left_border)
                    self.center_x = self.left_border
                if self.center_x < self.left_border:
                    self.dispatch(
                        'on_border', 'left', self.center_x, self.right_border)
                    self.center_x = self.right_border
            if self.top_border is not None and self.bottom_border is not None:
                if self.center_y > self.top_border:
                    self.dispatch(
                        'on_border', 'top', self.center_y, self.bottom_border)
                    self.center_y = self.bottom_border
                if self.center_y < self.bottom_border:
                    self.dispatch(
                        'on_border', 'bottom', self.center_y, self.top_border)
                    self.center_y = self.top_border
        else:
            raise ValueError(
                "Not known border exceeded logic: %s" %
                self.on_border_exceeded)

    def _next_flight_height(self):
        flight_height_factor = random()
        corridor_height = self.flight_height_dispersion * 2
        corridor_lower_point = (
            self.flight_height_middle - self.flight_height_dispersion)
        return flight_height_factor * corridor_height + corridor_lower_point

    def _next_velocity(self):
        velocity_factor = random()
        velocity_corridor = self.velocity_dispersion * 2
        velocity_lower_point = self.velocity_middle - self.velocity_dispersion
        return velocity_factor * velocity_corridor + velocity_lower_point

    def _setup_start_state(self):
        self._renew_traits()
        self.center_x = random() * (self.right_border - self.left_border)
        self.center_y = self.flight_height

    def _renew_traits(self, *_):
        self.flight_height = self._next_flight_height()
        self.velocity = self._next_velocity()
