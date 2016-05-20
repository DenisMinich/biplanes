from kivy.properties import ObjectProperty

from biplanes.entities import Plane
from biplanes.entities.blue_plane.states import (
    PlaneStateOnStart, PlaneStateNormal, PlaneStateDamaged,
    PlaneStateCriticalDamaged, PlaneStateNoPilot, PlaneStateBang,
    PlaneStateHidden)
from biplanes.entities.plane.plane_states import PlaneStates


class BluePlane(Plane):

    texuture = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super(BluePlane, self).__init__(
           *args, states=[
               PlaneStateOnStart, PlaneStateNormal, PlaneStateDamaged,
               PlaneStateCriticalDamaged, PlaneStateNoPilot, PlaneStateBang,
               PlaneStateHidden],
           **kwargs)
        self.change_state(PlaneStates.STATE_ON_START)
