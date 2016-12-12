"""RightButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class RightButton(BaseButton):
    """Tilt pilot to the right"""

    def update(self):
        if self._target.parachute is not None:
            if self._target.parachute.canopy is not None:
                self._target.parachute.canopy.is_tilted_right = self.touched
