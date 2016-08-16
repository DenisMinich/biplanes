"""Explosion implementation"""

from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget


class Explosion(Widget):
    """Explosion effect after plane destruction"""

    _texture = ObjectProperty()

    def __init__(self):
        super(Explosion, self).__init__(self)
        self._texture = Image(source='explosion.gif').texture
