from biplanes.controllers.base import BaseControl
from biplanes.controllers.manual.widgets.clockwise import ClockWiseButton
from biplanes.controllers.manual.widgets.conterclockwise import ConterClockWiseButton
from biplanes.controllers.manual.widgets.down import DownButton
from biplanes.controllers.manual.widgets.fire import FireButton
from biplanes.controllers.manual.widgets.info import Info
from biplanes.controllers.manual.widgets.up import UpButton


class ManualControl(BaseControl):

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
        self._target = target
        for control in self._controls:
            control.assign(target)

    def unassign(self):
        for control in self._controls:
            control.unassign(target)
