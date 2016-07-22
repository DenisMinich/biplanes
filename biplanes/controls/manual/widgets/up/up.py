"""UpButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class UpButton(BaseButton):
    """Button for plane acceleration"""

    def _accelerate(self, *_):
        """Accelerate plane"""
        self._target.increase_velocity()

    def _on_unassign(self):
        """Actions before unassign button"""
        self._target.unbind(on_update=self._accelerate)

    def _touch_down(self):
        """Perform actions on touch down"""
        self._target.bind(on_update=self._accelerate)

    def _touch_up(self):
        """Perform actions on touch up"""
        self._target.unbind(on_update=self._accelerate)
