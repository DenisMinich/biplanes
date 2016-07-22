"""PlaneStateDamaged implementation"""

from kivy.uix.image import Image

from biplanes.planes.standart.enums import PlaneStates


# pylint: disable=too-few-public-methods
class PlaneStateDamaged(object):
    """State when plane got some damage"""

    texture = Image(source='biplanes/data/blue_plane.png').texture
    name = PlaneStates.STATE_DAMAGED

    @staticmethod
    def on_apply(plane):
        """Action on state applying"""
        plane.texture = PlaneStateDamaged.texture
