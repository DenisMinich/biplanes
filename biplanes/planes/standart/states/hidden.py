"""PlaneStateBang implementation"""

from biplanes.planes.standart.enums import PlaneStates


# pylint: disable=too-few-public-methods
class PlaneStateHidden(object):
    """State when plane was destroyed and is waiting for respawn"""

    name = PlaneStates.STATE_HIDDEN

    @staticmethod
    def on_apply(plane):
        """Action on state applying"""
        plane.scene.planes.remove(plane)
        plane.delete_from_collections(['game_objects'])
        plane.add_to_collections(['hidden_objects'])
        PlaneStateHidden.unbind_actions(owner)
        plane.size = (0, 0)
        plane.plan_action(60, owner.change_state, PlaneStates.STATE_ON_START)

    @staticmethod
    def unbind_actions(plane):
        plane.unbind(on_update=owner._apply_arteficial_velocity)
        plane.unbind(on_update=owner._return_to_scene)
        plane.unbind(fixed_velocity=owner._check_takeoff_point)
        plane.unbind(fixed_velocity=owner._update_lift)
        plane.unbind(on_collide=owner._process_collissions)

