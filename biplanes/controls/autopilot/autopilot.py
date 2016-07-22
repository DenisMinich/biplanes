"""Autopilot implementation"""

from biplanes.controls.base.base import BaseControl


# pylint: disable=too-many-ancestors
class Autopilot(BaseControl):
    """Controls plane if there is no pilot"""

    def assign(self, target):
        self._target = target
        target.bind(on_update=self.update)

    def unassign(self):
        self._target = None
        self._target.unbind(on_update=self.update)

    def update(self, *args, **kwargs):
        self._target.decrease_velocity()
