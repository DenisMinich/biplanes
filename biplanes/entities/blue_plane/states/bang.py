from kivy.uix.image import Image
from kivy.vector import Vector

from biplanes.entities.plane.plane_states import PlaneStates


class PlaneStateBang(object):

    source = Image(source='data/bang.gif')
    name = PlaneStates.STATE_BANG

    @staticmethod
    def on_apply(owner):
        owner.texture = PlaneStateBang.source.texture
        owner.delete_from_collections(['planes'])
        owner.lift.gravity = Vector(0, 0)
        owner.move_stop()
        owner.fixed_velocity = 0
        owner.pos = (owner.center_x - 32, owner.center_y - 32)
        owner.size = (64, 64)
        owner.source = 'bang.gif'
        owner.plan_action(30, owner.change_state, PlaneStates.STATE_HIDDEN)
