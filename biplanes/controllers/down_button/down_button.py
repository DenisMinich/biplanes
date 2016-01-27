from kivy.uix.widget import Widget
from kivy.vector import Vector


class DownButton(Widget):
    def __init__(self, plane, *args, **kwargs):
        super(DownButton, self).__init__(*args, **kwargs)
        self.plane = plane

    def update_engine(self, *args):
        self.plane.engine.gravity += Vector(-.04, 0)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.plane.bind(on_update=self.update_engine)

    def on_touch_up(self, touch):
        self.plane.unbind(on_update=self.update_engine)
