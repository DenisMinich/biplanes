"""ConterClockWiseButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class ConterClockWiseButton(BaseButton):
    """Rotate plane conterclockwise button"""

    def _update_angle(self):
        """Change direction angle of plane"""
        if self._target.is_in_air:
            self._target.rotate_conterclockwise()

    def update(self):
        if self.touched:
            self._update_angle()
