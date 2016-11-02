"""EjectButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class EjectButton(BaseButton):
    """Eject pilot from a plane"""

    def update(self):
        """Perform actions on touch down"""
        if self.touched:
            self._target.eject()
