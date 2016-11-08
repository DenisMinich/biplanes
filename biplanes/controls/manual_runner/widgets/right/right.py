"""RunRightButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class RunRightButton(BaseButton):
    """Command pilot to run in right direction"""

    def update(self):
        self._target.is_run_right = self.touched
