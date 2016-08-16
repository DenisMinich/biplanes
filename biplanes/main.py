"""Main module of the app and contains main app class."""

from kivy.app import App
from parabox.base_object import BaseObject

from biplanes.controls.enums import Control
from biplanes.controls.factory import ControlFactory
from biplanes.pilots import enums as pilots_enums
from biplanes.pilots.factory import PilotFactory
from biplanes.planes import enums as planes_enums
from biplanes.planes.factory import PlaneFactory
from biplanes.scenes import enums as scenes_enums
from biplanes.scenes.factory import SceneFactory


class BiplanesClassicLevel(BaseObject):
    """Classic biplanes level"""

    _scene = None

    @property
    def scene(self):
        """Scene property"""
        return self._scene

    def __init__(self, *args, **kwargs):
        super(BiplanesClassicLevel, self).__init__(*args, **kwargs)
        self._control_factory = ControlFactory()
        self._plane_factory = PlaneFactory()
        self._scene_factory = SceneFactory()
        self._pilot_factory = PilotFactory()
        self._create_scene()
        self._create_player_plane()
        self._create_opponent_plane()

    def _create_scene(self):
        self._scene = self._scene_factory.get_scene(
            scenes_enums.Scene.BIPLANES_CLASSIC)

    def _create_player_plane(self):
        blue_plane = PlaneFactory.get_plane(planes_enums.PlaneModel.STANDART)
        blue_plane.team = planes_enums.Team.BLUE_TEAM
        blue_plane.control = self._control_factory.get_control(
            Control.PLAYER_CONTROL)
        blue_plane.bind(on_destroy=self._process_player_plane_destroyed)
        blue_plane.bind(on_ejection=self._process_player_plane_ejected)
        self._scene.add_widget(blue_plane)
        self._scene.add_widget(blue_plane.control)

    def _process_player_plane_destroyed(self, plane, cause):
        self._scene.remove_widget(plane)
        self._scene.remove_widget(plane.control)
        self._scene.add_effect(self._scene_factory.get_decoration(
            scenes_enums.Decoration.EXPLOSION))
        if plane.is_contains_pilot:
            self._process_player_death(plane.pilot, cause)

    def _process_player_plane_ejected(self, plane):
        self._scene.remove_widget(plane.control)
        plane.control = self._control_factory.get_control(
            Control.AUTOPILOT)
        pilot = self._pilot_factory.get_pilot(pilots_enums.Pilot.DEFAULT_PILOT)
        pilot.control = self._control_factory.get_control(
            Control.PLAYER_PILOT_CONTROL)
        pilot.bind(on_kill=self._process_player_pilot_killed)
        pilot.bind(on_achieve=self._process_player_achieved_spawn)
        self._scene.add_widget(pilot)
        self._scene.add_widget(pilot.control)

    def _process_player_pilot_killed(self, pilot, cause):
        self._scene.remove_widget(pilot)
        self._scene.remove_widget(pilot.control)
        self._scene.add_effect(self._scene_factory.get_decoration(
            scenes_enums.Decoration.DEATH_ANIMATION))
        self._process_player_death(pilot.player, cause)

    def _process_player_achieved_spawn(self, pilot):
        self._scene.remove_widget(pilot)
        self._scene.remove_widget(pilot.control)
        self._create_player_plane()

    def _create_opponent_plane(self):
        red_plane = PlaneFactory.get_plane(planes_enums.PlaneModel.STANDART)
        red_plane.team = planes_enums.Team.RED_TEAM
        red_plane.control = self._control_factory.get_control(
            Control.AI_BEGINNER)
        red_plane.bind(on_destroy=self._process_ai_plane_destroyed)
        red_plane.bind(on_ejection=self._process_ai_plane_ejected)
        self._scene.add_widget(red_plane)

    def _process_ai_plane_destroyed(self, plane, cause):
        self._scene.remove_widget(plane)
        self._scene.add_effect(self._scene_factory.get_decoration(
            scenes_enums.Decoration.EXPLOSION))
        if plane.is_contains_pilot:
            self._process_player_death(plane.player, cause)

    def _process_ai_plane_ejected(self, plane):
        plane.control = self._control_factory.get_control(
            Control.AUTOPILOT)
        pilot = self._pilot_factory.get_pilot(pilots_enums.Pilot.DEFAULT_PILOT)
        pilot.control = self._control_factory.get_control(
            Control.AI_BEGINNER_PILOT)
        pilot.bind(on_kill=self._process_ai_pilot_killed)
        pilot.bind(on_achieve=self._process_ai_achieved_spawn)
        self._scene.add_widget(pilot)

    def _process_ai_pilot_killed(self, pilot, cause):
        self._scene.remove_widget(pilot)
        self._scene.add_effect(self._scene_factory.get_decoration(
            scenes_enums.Decoration.DEATH_ANIMATION))
        self._process_player_death(pilot.player, cause)

    def _process_ai_achieved_spawn(self, pilot):
        self._scene.remove_widget(pilot)
        self._create_opponent_plane()

    def _process_player_death(self, player, cause):
        pass


class GameApp(App):
    """Main class of the application."""

    def build(self):
        """Should return main widget"""
        return BiplanesClassicLevel().scene

if __name__ == "__main__":
    GameApp().run()
