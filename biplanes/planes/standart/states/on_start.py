from kivy.uix.image import Image
from kivy.vector import Vector

from biplanes import settings as global_settings
from biplanes.entities.plane.plane_states import PlaneStates


class PlaneStateOnStart(object):

    source = Image(source='data/blue_plane.png')
    name = PlaneStates.STATE_ON_START

    @staticmethod
    def on_apply(owner):
        owner.texture = PlaneStateOnStart.source.texture
        owner.delete_from_collections(['hidden_objects'])
        owner.add_to_collections(['planes', 'game_objects'])
        PlaneStateOnStart._bind_actions(owner)
        owner.lift.gravity = Vector(0, global_settings.GLOBAL_GRAVITY)
        owner.size = (50, 50)
        owner.pos = (20, 42)
        owner.in_air = False
        owner.points = 3
        owner.fixed_velocity = 0

    @staticmethod
    def _bind_actions(owner):
        owner.bind(on_update=owner._apply_arteficial_velocity)
        owner.bind(on_update=owner._return_to_scene)
        owner.bind(fixed_velocity=owner._check_takeoff_point)
        owner.bind(fixed_velocity=owner._update_lift)
        owner.bind(on_collide=owner._process_collissions)
