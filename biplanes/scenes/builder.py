"""Scene builder implementation"""

from kivy.uix.image import Image

from biplanes.entities.ground import Ground
from biplanes.scenes.enums import Scene
from biplanes.scenes.exceptions import SceneBuilderError


class SceneBuilder(object):  # pylint: disable=too-few-public-methods
    """Creates scenes (environment objects) by scene name"""

    def __init__(self, scene_owner):
        """Class constructor"""
        self._scene_owner = scene_owner

    def create_scene(self, scene_name):
        """Creates environment

        :param scene_name: name of scene to create
        :type scene_name: str
        """
        if scene_name == Scene.BIPLANES_CLASSIC:
            self._scene_owner.texture = Image(source='background.png').texture
            self._scene_owner.environment.add(
                Ground(pos=(0, 0), size=(800, 40)))
        else:
            raise SceneBuilderError("Unknown scene name")
