"""Autopilot implementation"""

from biplanes.controls.base import base as base_control


# pylint: disable=too-many-ancestors
class Autopilot(base_control.BaseControl):
    """Controls plane if there is no pilot"""

    def assign(self, target):
        self._target = target
        target.bind(on_update=self.update)

    def unassign(self):
        self._target = None
        self._target.unbind(on_update=self.update)

    def update(self):
        if self._target.is_in_air:
            self._target.decrease_velocity()
