"""BluePlaneTexturesPack implementation"""

from kivy.resources import resource_find
from kivy.uix.image import Image

from biplanes.textures.base import BaseTexturesPack


# pylint: disable=too-few-public-methods
# pylint: disable=missing-docstring
class BluePlaneTexturesPack(BaseTexturesPack):
    """Contains textures of blue plane"""

    @property
    def plane_on_start(self):
        return Image(source=resource_find('blue_plane.png')).texture

    @property
    def plane_normal(self):
        return Image(source=resource_find('blue_plane.png')).texture

    @property
    def plane_damaged(self):
        return Image(source=resource_find('blue_plane.png')).texture

    @property
    def plane_critical_damaged(self):
        return Image(source=resource_find('blue_plane.png')).texture
