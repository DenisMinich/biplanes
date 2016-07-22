"""DownButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class DownButton(BaseButton):
    """Speed down button"""

    def _decrease_velocity(self, *_):
        """Decrease velocity of a plane"""
        self._target.decrease_velocity()

    def _on_unassign(self):
        """Actions before unassign button"""
        self._target.unbind(on_update=self._decrease_velocity)

    def _touch_down(self):
        """Perform actions on touch down"""
        self._target.bind(on_update=self._decrease_velocity)

    def _touch_up(self):
        """Perform actions on touch up"""
        self._target.unbind(on_update=self._decrease_velocity)
