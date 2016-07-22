"""ConterClockWiseButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class ConterClockWiseButton(BaseButton):
    """Rotate plane conterclockwise button"""

    def _update_angle(self, *_):
        """Change direction angle of plane"""
        if self._target.is_in_air:
            self._target.rotate_conterclockwise()

    def _on_unassign(self):
        """Actions before unassign button"""
        self._target.unbind(on_update=self._update_angle)

    def _touch_down(self):
        """Perform actions on touch down"""
        self._target.bind(on_update=self._update_angle)

    def _touch_up(self):
        """Perform actions on touch up"""
        self._target.unbind(on_update=self._update_angle)
