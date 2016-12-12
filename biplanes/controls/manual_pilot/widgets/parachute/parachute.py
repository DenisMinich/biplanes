"""ParachuteButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class ParachuteButton(BaseButton):
    """Open parachute or disconnect it"""

    _untouched = True
    """Is button was released after last touching"""

    def update(self):
        """Perform actions on touch down

        .. note:: _untouched property impemented to prevent
            disconnecting parachute after it was just opened
            because of player hasn't released button
        """
        if self.touched:
            if self._untouched:
                self._target.parachute.pull_the_ring()
                self._untouched = False
        else:
            self._untouched = True
