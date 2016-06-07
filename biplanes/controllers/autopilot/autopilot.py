from biplanes.controllers.base import BaseControl


class Autopilot(BaseControl):

    def assign(self, target):
        self._target = target
        target.bind(on_update=self.update)

    def unassign(self):
        self._target = None
        target.unbind(on_update=self.update)

    def update(self, *args, **kwargs):
        target.decrease_velocity()
