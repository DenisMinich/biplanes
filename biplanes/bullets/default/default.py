"""DefaultBullet implementation"""

from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget


class DefaultBullet(Widget):
    """Base plane bullet widget"""

    _texture = ObjectProperty()

    _plane = ObjectProperty()

    def __init__(self, *args, source=None, angle=None, **kwargs):
        super(DefaultBullet, self).__init__(*args, **kwargs)
        self._texture = Image(source='bullet_default.png').texture
        self._size = (5, 5)
        self._source = source
        self._angle = angle
