"""UpButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class UpButton(BaseButton):
    """Button for plane acceleration"""

    def _accelerate(self):
        """Accelerate plane"""
        self._target.increase_velocity()

    def update(self):
        """Perform actions on touch down"""
        if self.touched:
            self._accelerate()
