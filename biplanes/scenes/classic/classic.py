"""BiplanesClassicScene implementation"""

from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget


class BiplanesClassicScene(Widget):
    """Base scene"""

    texture = ObjectProperty()

    def __init__(self):
        super(BiplanesClassicScene, self).__init__()
        self.texture = Image(source='background.png').texture
