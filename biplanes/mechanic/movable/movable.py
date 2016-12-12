"""Movable implementation"""

from kivy import properties
from kivy import vector

from biplanes.base_entity import BaseEntity


class Movable(BaseEntity):  # pylint: disable=too-many-ancestors
    """Extends widget with movement traits"""

    angle = properties.NumericProperty()
    """Rotation angle"""

    def get_velocity(self):  # pylint: disable=no-self-use
        """Vector of velocity"""
        return vector.Vector(0, 0)

    velocity = properties.AliasProperty(get_velocity)
    """Movement velocity"""

    def move(self):
        """Update object's position based on it's velocity"""
        self.pos = (
            self.pos[0] + self.velocity[0],
            self.pos[1] + self.velocity[1])
