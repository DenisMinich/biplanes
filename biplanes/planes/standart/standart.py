"""Standart biplane implementation"""

from biplanes.planes.base.base import BasePlane


# pylint: disable=duplicate-bases,too-many-ancestors
class StandartPlane(BasePlane):
    """Standart biplane"""
    points = 5

    @staticmethod
    def on_points(self, value):
        if value == 3:
            self.change_state(PlaneStates.STATE_NORMAL)
        elif value == 2:
            self.change_state(PlaneStates.STATE_DAMAGED)
        elif value == 1:
            self.change_state(PlaneStates.STATE_CRITICAL_DAMAGED)
        elif value == 0:
            self.change_state(PlaneStates.STATE_BANG)
