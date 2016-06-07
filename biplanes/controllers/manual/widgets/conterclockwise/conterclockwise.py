from biplanes.controllers.manual.widgets.base import BaseButton


class ConterClockWiseButton(BaseButton):
    def update_angle(self, *args):
        if self._target.in_air:
            self._target.angle += 3

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self._target.bind(on_update=self.update_angle)

    def on_touch_up(self, touch):
        self._target.unbind(on_update=self.update_angle)