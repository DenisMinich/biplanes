"""DownButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class DownButton(BaseButton):
    """Speed down button"""

    def _decrease_velocity(self):
        """Decrease velocity of a plane"""
        self._target.decrease_velocity()

    def update(self):
        if self.touched:
            self._decrease_velocity()
