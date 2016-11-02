"""LeftButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class LeftButton(BaseButton):
    """Tilt pilot to the left"""

    def update(self):
        self._target.tilt_left = self.touched
