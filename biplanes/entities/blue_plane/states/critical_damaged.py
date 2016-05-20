from kivy.uix.image import Image

from biplanes.entities.plane.plane_states import PlaneStates


class PlaneStateCriticalDamaged(object):

    source = Image(source='data/blue_plane.png')
    name = PlaneStates.STATE_CRITICAL_DAMAGED

    @staticmethod
    def on_apply(owner):
        owner.texture = PlaneStateCriticalDamaged.source.texture
