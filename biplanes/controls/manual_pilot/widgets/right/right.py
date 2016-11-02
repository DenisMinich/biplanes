"""RightButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class RightButton(BaseButton):
    """Tilt pilot to the right"""

    def update(self):
        self._target.tilt_right = self.touched
