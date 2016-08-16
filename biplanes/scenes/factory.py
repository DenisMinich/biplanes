"""SceneFactory implementation"""

from biplanes.scenes.classic.classic import BiplanesClassicScene
from biplanes.scenes.enums import Decoration
from biplanes.scenes.enums import Scene
from biplanes.scenes.exceptions import SceneFactoryError
from biplanes.scenes.decorations.explosion import Explosion


class SceneFactory(object):  # pylint: disable=too-few-public-methods
    """Creates scenes by scene name"""

    @staticmethod
    def get_scene(scene_name):
        """Returns scene widget by it's name

        :param scene_name: name of scene to create
        :type scene_name: str
        """
        if scene_name == Scene.BIPLANES_CLASSIC:
            return BiplanesClassicScene()
        else:
            raise SceneFactoryError("Unknown scene name")

    @staticmethod
    def get_decoration(decoration_name):
        """Returns scene decoration widget by it's name

        :param decoration_name: name of decoration to create
        :type decoration_name: str
        """
        if decoration_name == Decoration.EXPLOSION:
            return Explosion()
        else:
            raise SceneFactoryError("Unknown decoration name")
