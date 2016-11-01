"""Movable implementation"""

from biplanes.base_entity import BaseEntity


class Movable(BaseEntity):
    """Extends widget with movement traits"""

    angle = properties.NumericProperty()
    """Rotation angle"""

    velocity = properties.NumericProperty()
    """Movement velocity"""

    @property
    def velocity_vector(self):
        """Vector of velocity"""
        return Vector(self.velocity, 0).rotate(self.angle)

    def move(self):
        self.pos = (
            self.pos[0] + self.velocity_vector[0],
            self.pos[1] + self.velocity_vector[1])
