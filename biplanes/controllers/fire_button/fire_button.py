from kivy.uix.widget import Widget
from kivy.vector import Vector
from parabox.structures.collector import Collector


class FireButton(Widget):
    def __init__(self, plane, *args, **kwargs):
        super(FireButton, self).__init__(*args, **kwargs)
        self.plane = plane

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            if len(Collector.get_collection('bullets')) < 3:
                self.plane.fire()
