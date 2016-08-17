"""BiplanesClassicScene implementation"""

from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget

from biplanes.entities.ground.ground import Ground


class BiplanesClassicScene(Widget):
    """Base scene"""

    texture = ObjectProperty()

    def __init__(self):
        super(BiplanesClassicScene, self).__init__()
        self.texture = Image(source='background.png').texture
        self.add_widget(Ground(pos=(0, 0), size=(800, 40)))

    def add_effect(self, effect):
        """Add temporary visual effect"""
        self.add_widget(effect)
        effect.bind(on_finish=self.remove_widget)
