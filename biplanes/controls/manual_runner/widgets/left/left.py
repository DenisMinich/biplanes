"""RunLeftButton implementation"""

from biplanes.controls.manual.widgets.base.base import BaseButton


class RunLeftButton(BaseButton):
    """Command pilot to run in left direction"""

    def update(self):
        self._target.is_run_left = self.touched
