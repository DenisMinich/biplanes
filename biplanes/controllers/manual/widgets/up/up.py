from kivy.vector import Vector

from biplanes.controllers.manual.widgets.base import BaseButton


class UpButton(BaseButton):
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self._target.bind(on_update=self._target.increase_velocity)

    def on_touch_up(self, touch):
        self._target.unbind(on_update=self._target.increase_velocity)
