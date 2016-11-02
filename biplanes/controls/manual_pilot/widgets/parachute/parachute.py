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
        if self.touched and self._untouched:
            if self._target.with_parachute:
                self._target.disconnect_parachute()
            elif self._target.has_parachute:
                self._target.open_parachute()
            self._untouched = False
        else:
            self._untouched = True
