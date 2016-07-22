"""FireButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class FireButton(BaseButton):
    """Fire bullet from a plane's gun"""

    def _touch_down(self):
        """Perform actions on touch down"""
        self._target.fire()
