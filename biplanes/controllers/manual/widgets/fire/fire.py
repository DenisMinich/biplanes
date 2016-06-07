from kivy.vector import Vector
from parabox.structures.collector import Collector

from biplanes.controllers.manual.widgets.base import BaseButton


class FireButton(BaseButton):
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            if len(Collector.get_collection('bullets')) < 3:
                self._target.fire()
