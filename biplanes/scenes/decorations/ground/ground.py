"""Ground implementation"""

from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

from biplanes.base_entity import BaseEntity


class Ground(BaseEntity):
    """Ground layer on the bottom of the scene"""

    texture = ObjectProperty()

    scene = ObjectProperty()

    tags = ListProperty(["decoration", "solid"])

    def __init__(self, *args, scene=None, **kwargs):
        self.scene = scene
        super(Ground, self).__init__(*args, **kwargs)
        self.texture = Image(source='ground.png').texture
        self.texture.wrap = 'repeat'
        self.texture.uvsize = (8, 1)
