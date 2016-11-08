"""Barn implementation"""

from kivy import properties
from kivy.uix.image import Image

from biplanes.base_entity import BaseEntity


# pylint: disable=too-many-instance-attributes
class Barn(BaseEntity):
    """Barn decoration"""

    texture = properties.ObjectProperty()
    """Self texture"""

    tags = properties.ListProperty(["solid", "spawn"])
    """Tags for object"""

    def __init__(self, *args, **kwargs):
        self.texture = Image(source='barn.png').texture
        super(Barn, self).__init__(*args, **kwargs)
