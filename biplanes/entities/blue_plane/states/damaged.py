from kivy.uix.image import Image

from biplanes.entities.plane.plane_states import PlaneStates


class PlaneStateDamaged(object):

    source = Image(source='data/blue_plane.png')
    name = PlaneStates.STATE_DAMAGED

    @staticmethod
    def on_apply(owner):
        owner.texture = PlaneStateDamaged.source.texture
