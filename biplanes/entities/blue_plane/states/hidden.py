from biplanes.entities.plane.plane_states import PlaneStates


class PlaneStateHidden(object):

    name = PlaneStates.STATE_HIDDEN

    @staticmethod
    def on_apply(owner):
        owner.delete_from_collections(['game_objects'])
        owner.add_to_collections(['hidden_objects'])
        PlaneStateHidden.unbind_actions(owner)
        owner.size = (0, 0)
        owner.plan_action(60, owner.change_state, PlaneStates.STATE_ON_START)

    @staticmethod
    def unbind_actions(owner):
        owner.unbind(on_update=owner._apply_arteficial_velocity)
        owner.unbind(on_update=owner._return_to_scene)
        owner.unbind(fixed_velocity=owner._check_takeoff_point)
        owner.unbind(fixed_velocity=owner._update_lift)
        owner.unbind(on_collide=owner._process_collissions)

