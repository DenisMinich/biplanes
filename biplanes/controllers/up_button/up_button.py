from kivy.logger import Logger
from kivy.uix.widget import Widget
from kivy.vector import Vector


class UpButton(Widget):
    def __init__(self, plane, *args, **kwargs):
        super(UpButton, self).__init__(*args, **kwargs)
        self.plane = plane

    def update_engine(self, *args):
        self.plane.engine.gravity += Vector(.02, 0)
        Logger.info('engine_up: %s' % self.plane.engine.gravity)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            Logger.info('up touch down')
            self.plane.bind(on_update=self.update_engine)

    def on_touch_up(self, touch):
        Logger.info('up touch up')
        self.plane.unbind(on_update=self.update_engine)
