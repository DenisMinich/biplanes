"""SceneFactory implementation"""

from biplanes.scenes.classic.classic import BiplanesClassicScene
from biplanes.scenes.enums import Scene
from biplanes.scenes.exceptions import SceneFactoryError


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
