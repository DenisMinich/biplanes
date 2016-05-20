from kivy.uix.image import Image

from biplanes.entities.plane.plane_states import PlaneStates


class PlaneStateNoPilot(object):

    source = Image(source='data/blue_plane.png')
    name = PlaneStates.STATE_NO_PILOT

    @staticmethod
    def on_apply(owner):
        owner.texture = PlaneStateNoPilot.source.texture
