"""TextureFactory implementation"""

from biplanes.textures.enums import TexturePackModel
from biplanes.textures.exceptions import TextureFactoryError
from biplanes.textures.planes.blue_plane.blue_plane import (
    BluePlaneTexturesPack)
from biplanes.textures.planes.red_plane.red_plane import RedPlaneTexturesPack


class TextureFactory(object):  # pylint: disable=too-few-public-methods
    """Returns textures pack by it's name"""

    @staticmethod
    def get_textures_pack(texture_name):
        """Returns texture widget by it's name

        :param texture_name: name of texture to create
        :type texture_name: str
        """
        if texture_name == TexturePackModel.BLUE_PLANE:
            return BluePlaneTexturesPack()
        if texture_name == TexturePackModel.RED_PLANE:
            return RedPlaneTexturesPack()
        else:
            raise TextureFactoryError("Unknown texture name")
