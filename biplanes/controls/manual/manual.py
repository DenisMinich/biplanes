"""Player control"""

from biplanes.controls.base.base import BaseControl
from biplanes.controls.manual.widgets.clockwise.clockwise import (
    ClockWiseButton)
from biplanes.controls.manual.widgets.conterclockwise.conterclockwise import (
    ConterClockWiseButton)
from biplanes.controls.manual.widgets.down.down import DownButton
from biplanes.controls.manual.widgets.fire.fire import FireButton
from biplanes.controls.manual.widgets.up.up import UpButton


class ManualControl(BaseControl):  # pylint: disable=too-many-ancestors
    """Control for player"""

    def __init__(self, *args, **kwargs):
        super(ManualControl, self).__init__(*args, **kwargs)
        self._clockwise = ClockWiseButton()
        self._conterclockwise = ConterClockWiseButton()
        self._down = DownButton()
        self._fire = FireButton()
        self._up = UpButton()
        self._controls = [
            self._clockwise, self._conterclockwise, self._down,
            self._fire, self._up]
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
