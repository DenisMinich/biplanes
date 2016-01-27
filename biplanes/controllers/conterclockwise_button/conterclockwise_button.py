from kivy.uix.widget import Widget


class ConterClockWiseButton(Widget):
    def __init__(self, plane, *args, **kwargs):
        super(ConterClockWiseButton, self).__init__(*args, **kwargs)
        self.plane = plane

    def update_angle(self, *args):
        self.plane.angle += 3

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.plane.bind(on_update=self.update_angle)

    def on_touch_up(self, touch):
        self.plane.unbind(on_update=self.update_angle)
