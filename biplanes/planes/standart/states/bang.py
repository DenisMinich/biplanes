"""PlaneStateBang implementation"""

from kivy.uix.image import Image

from biplanes.planes.standart.enums import PlaneStates


# pylint: disable=too-few-public-methods
class PlaneStateBang(object):
    """State when plane become pile of scrap"""

    texture = Image(source='biplanes/data/bang.gif').texture
    texture_size = (64, 64)
    name = PlaneStates.STATE_BANG

    @staticmethod
    def on_apply(plane):
        """Action on state applying"""
        plane.texture = PlaneStateBang.texture
        plane.scene.planes.remove(plane)
        plane.velocity = 0
        plane.pos = (
            plane.center_x - PlaneStateBang.texture_size[0],
            plane.center_y - PlaneStateBang.texture_size[1])
        plane.size = PlaneStateBang.texture_size
        plane.plan_action(30, plane.change_state, PlaneStates.STATE_HIDDEN)
