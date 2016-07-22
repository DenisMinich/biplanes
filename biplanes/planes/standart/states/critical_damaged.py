"""PlaneStateCriticalDamaged implementation"""

from kivy.uix.image import Image

from biplanes.planes.standart.enums import PlaneStates


# pylint: disable=too-few-public-methods
class PlaneStateCriticalDamaged(object):
    """State when plane looks very damaged"""

    texture = Image(source='biplanes/data/blue_plane.png').texture
    name = PlaneStates.STATE_CRITICAL_DAMAGED

    @staticmethod
    def on_apply(plane):
        """Action on state applying"""
        plane.texture = PlaneStateCriticalDamaged.texture
