"""Player control for pilot in air"""

from biplanes.controls.base import base
from biplanes.controls.manual_pilot.widgets.left import left
from biplanes.controls.manual_pilot.widgets.parachute import parachute
from biplanes.controls.manual_pilot.widgets.right import right


# pylint: disable=too-many-ancestors
# pylint: disable=too-many-instance-attributes
class ManualPilotControl(base.BaseControl):
    """Control for player"""

    def __init__(self, *args, **kwargs):
        super(ManualPilotControl, self).__init__(*args, **kwargs)
        self._left = left.LeftButton()
        self._right = right.RightButton()
        self._parachute = parachute.ParachuteButton()
        self._controls = [self._left, self._right, self._parachute]
        for control in self._controls:
            self.add_widget(control)

    def assign(self, target):
        """Assign all inner controls to target plane

        :param target: plane to control by target
        :type target: biplanes.entities.plane.plane.Plane
        """
        self._target = target
        for control in self._controls:
            control.assign(target)

    def unassign(self):
        """Unassign all inner controls from target plane"""
        for control in self._controls:
            control.unassign()

    def update(self):
        """Update all inner controls state"""
        for control in self._controls:
            control.update()
