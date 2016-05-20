from kivy.uix.image import Image

from biplanes.entities.plane.plane_states import PlaneStates


class PlaneStateNormal(object):

    source = Image(source='data/blue_plane.png')
    name = PlaneStates.STATE_NORMAL

    @staticmethod
    def on_apply(owner):
        owner.texture = PlaneStateNormal.source.texture
