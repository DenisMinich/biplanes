"""Player control"""

from biplanes.controls.base import base
from biplanes.controls.manual.widgets.clockwise import clockwise
from biplanes.controls.manual.widgets.conterclockwise import conterclockwise
from biplanes.controls.manual.widgets.down import down
from biplanes.controls.manual.widgets.eject import eject
from biplanes.controls.manual.widgets.fire import fire
from biplanes.controls.manual.widgets.up import up


# pylint: disable=too-many-ancestors
# pylint: disable=too-many-instance-attributes
class ManualControl(base.BaseControl):
    """Control for player"""

    def __init__(self, *args, **kwargs):
        super(ManualControl, self).__init__(*args, **kwargs)
        self._clockwise = clockwise.ClockWiseButton()
        self._conterclockwise = conterclockwise.ConterClockWiseButton()
        self._down = down.DownButton()
        self._fire = fire.FireButton()
        self._up = up.UpButton()
        self._eject = eject.EjectButton()
        self._controls = [
            self._clockwise, self._conterclockwise, self._down,
            self._fire, self._up, self._eject]
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
