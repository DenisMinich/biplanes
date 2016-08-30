"""ClockWiseButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class ClockWiseButton(BaseButton):
    """Rotate plane clockwise button"""

    def _update_angle(self):
        """Change direction angle of plane"""
        if self._target.is_in_move:
            self._target.rotate_clockwise()

    def update(self):
        if self.touched:
            self._update_angle()
