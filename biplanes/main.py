"""Main module of the app and contains main app class."""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.resources import resource_add_path
from parabox.base_object import BaseObject

from biplanes.controls.builder import ControlBuilder
from biplanes.controls.enums import Control
from biplanes.planes.builder import PlaneBuilder
from biplanes.planes.enums import PlaneModel
from biplanes.planes.enums import Team
from biplanes.scenes.builder import SceneBuilder
from biplanes.scenes.enums import Scene
from biplanes.settings import STATIC_PATH


resource_add_path(STATIC_PATH)
Builder.load_file('game.kv')


class BiplanesClassicLevel(BaseObject):
    """Classic biplanes level"""

    texture = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super(BiplanesClassicLevel, self).__init__(*args, **kwargs)
        self._control_builder = ControlBuilder(self)
        self._plane_builder = PlaneBuilder(self)
        self._scene_builder = SceneBuilder(self)
        self._draw_scene()
        self._draw_planes()

    def _draw_scene(self):
        self._scene_builder.create_scene(
            Scene.BIPLANES_CLASSIC)

    def _draw_planes(self):
        self._plane_builder.create_plane(
            team=Team.BLUE_TEAM,
            model=PlaneModel.STANDART,
            control=self._control_builder.create_control(
                Control.PLAYER_CONTROL))
        self._plane_builder.create_plane(
            team=Team.RED_TEAM,
            model=PlaneModel.STANDART,
            control=self._control_builder.create_control(
                Control.AI_BEGINNER))


class GameApp(App):
    """Main class of the application."""

    def build(self):
        """Should return main widget"""
        return BiplanesClassicLevel()

if __name__ == "__main__":
    GameApp().run()
