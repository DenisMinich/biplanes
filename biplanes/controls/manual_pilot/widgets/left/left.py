"""LeftButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class LeftButton(BaseButton):
    """Tilt pilot to the left"""

    def update(self):
        if self._target.parachute is not None:
            if self._target.parachute.canopy is not None:
                self._target.parachute.canopy.is_tilted_left = self.touched
