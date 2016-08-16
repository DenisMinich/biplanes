"""DefaultPilot implementation"""

from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget


class DefaultPilot(Widget):
    """Base pilot widget"""

    _texture = ObjectProperty()

    def __init__(self):
        super(DefaultPilot, self).__init__(self)
        self._texture = Image(source='background.png').texture
