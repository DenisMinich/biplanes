from kivy.uix.widget import Widget
from kivy.vector import Vector


class UpButton(Widget):
    def __init__(self, plane, *args, **kwargs):
        super(UpButton, self).__init__(*args, **kwargs)
        self.plane = plane

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.plane.bind(on_update=self.plane.increase_velocity)

    def on_touch_up(self, touch):
        self.plane.unbind(on_update=self.plane.increase_velocity)
