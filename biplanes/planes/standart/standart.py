"""Standart biplane implementation"""

from biplanes.planes.base.base import BasePlane


# pylint: disable=duplicate-bases,too-many-ancestors
# pylint: disable=too-many-ancestors
# pylint: disable=too-many-instance-attributes
class StandartPlane(BasePlane):
    """Standart biplane"""

    TEXTURE_ON_START = None
    TEXTURE_NORMAL = None
    TEXTURE_DAMAGED = None
    TEXTURE_CRITICAL_DAMAGED = None

    def __init__(self):
        super(StandartPlane, self).__init__(self)
        self.takeoff_point = 4
        self.max_velocity = 5
        self.max_points = 3
        self.points = 3
        self.in_air = False
        self.in_move = False
        self.acceleration = .03
        self.braking = .03
        self.rotate_clockwise_velocity = 3
        self.rotate_conterclockwise_velocity = 3
        self.texture = self.TEXTURE_ON_START
        self.size = (50, 50)
        self.pos = (20, 42)

    def on_points(self, value):
        """Update planes state based on current points"""
        if value == 3:
            self.texture = self.TEXTURE_NORMAL
        elif value == 2:
            self.texture = self.TEXTURE_DAMAGED
        elif value == 1:
            self.texture = self.TEXTURE_CRITICAL_DAMAGED
        elif value == 0:
            self.destroy()
