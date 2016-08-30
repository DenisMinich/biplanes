"""FireButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class FireButton(BaseButton):
    """Fire bullet from a plane's gun"""

    def update(self):
        """Perform actions on touch down"""
        if self.touched:
            self._target.fire()
