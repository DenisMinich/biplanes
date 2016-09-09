"""Explosion implementation"""

from kivy.clock import Clock
from kivy import properties
from kivy.uix.image import Image

from biplanes.base_entity import BaseEntity


class Explosion(BaseEntity):
    """Explosion effect after plane destruction"""

    texture = properties.ObjectProperty()

    duration = properties.NumericProperty(1.5)

    def __init__(self, *args, center=None, **kwargs):
        self.source = Image(
            source='explosion.gif', anim_delay=.05,
            anim_loop=1, allow_stretch=True)
        super(Explosion, self).__init__(*args, **kwargs)
        self.size = (64, 64)
        self.pos = (center[0] - self.size[0] / 2, center[1] - self.size[1] / 2)
        Clock.schedule_once(self.end_effect, self.duration)

    def end_effect(self, *_):
        """Delete effect after it finish animation"""
        self.remove_item(self)
