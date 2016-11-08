"""ManualRunnerControl implementation"""

from biplanes.controls.base import base
from biplanes.controls.manual_runner.widgets.left import left
from biplanes.controls.manual_runner.widgets.right import right


# pylint: disable=too-many-ancestors
# pylint: disable=too-many-instance-attributes
class ManualRunnerControl(base.BaseControl):
    """Manual control for pilot on the ground"""

    def __init__(self, *args, **kwargs):
        super(ManualRunnerControl, self).__init__(*args, **kwargs)
        self._left = left.RunLeftButton()
        self._right = right.RunRightButton()
        self._controls = [self._left, self._right]
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
