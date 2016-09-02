"""Main module of the app and contains main app class."""

import os

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.resources import resource_add_path

from biplanes.controls.enums import Control
from biplanes.controls.factory import ControlFactory
from biplanes.planes import enums as planes_enums
from biplanes.planes.factory import PlaneFactory
from biplanes.scenes import enums as scenes_enums
from biplanes.scenes.factory import SceneFactory


# pylint: disable=too-few-public-methods
class BiplanesClassicLevel(object):
    """Classic biplanes level"""

    _scene = None

    _update_interval = .01

    _objects_to_update = None

    _clock = None

    @property
    def scene(self):
        """Scene property"""
        return self._scene

    def __init__(self):
        self._objects_to_update = set()
        self._create_scene()
        self._create_player_plane()
        self._start_level()

    def _start_level(self):
        """Setup update objects on schedule"""
        self._clock = Clock.schedule_interval(
            self._update_state, self._update_interval)

    def _update_state(self, *_):
        """Update inner objects"""
        for inner_object in self._objects_to_update:
            inner_object.update()

    def on_item_added(self, _, item):
        """Callback on new item created"""
        self.add_item(item)

    def on_item_removed(self, _, item):
        """Callback on item removed"""
        self.remove_item(item)

    def add_item(self, item):
        """Add item to the scene"""
        self._scene.add_widget(item)
        self._objects_to_update.add(item)
        item.bind(on_create=self.on_item_added)
        item.bind(on_remove=self.on_item_removed)

    def remove_item(self, item):
        """Remove item from the scene"""
        self._scene.remove_widget(item)
        self._objects_to_update.remove(item)
        item.unbind(on_create=self.on_item_added)
        item.unbind(on_remove=self.on_item_removed)

    def _create_scene(self):
        self._scene = SceneFactory.get_scene(
            scenes_enums.Scene.BIPLANES_CLASSIC)

    def _create_player_plane(self):
        blue_plane = PlaneFactory.get_plane(
            planes_enums.PlaneModel.STANDART, scene=self.scene)
        blue_plane.team = planes_enums.Team.BLUE_TEAM
        blue_plane.control = ControlFactory.get_control(
            Control.PLAYER_CONTROL)
        blue_plane.bind(on_destroy=self._process_player_plane_destroyed)
        blue_plane.bind(on_ejection=self._process_player_plane_ejected)
        self.add_item(blue_plane)
        self.add_item(blue_plane.control)

    def _process_player_plane_destroyed(self, plane, cause):
        self.remove_item(plane)
        self.remove_item(plane.controller)
        if plane.is_contains_pilot:
            self._process_player_death(plane.pilot, cause)

    def _process_player_plane_ejected(self, plane, pilot):
        self.remove_item(plane.controller)
        plane.control = ControlFactory.get_control(Control.AUTOPILOT)
        pilot.control = ControlFactory.get_control(
            Control.PLAYER_PILOT_CONTROL)
        pilot.bind(on_kill=self._process_player_pilot_killed)
        pilot.bind(on_achieve=self._process_player_achieved_spawn)
        self.add_item(pilot.control)

    def _process_player_pilot_killed(self, pilot, cause):
        self.remove_item(pilot)
        self.remove_item(pilot.control)
        self._process_player_death(pilot.player, cause)

    def _process_player_achieved_spawn(self, pilot):
        self.remove_item(pilot)
        self.remove_item(pilot.control)
        self._create_player_plane()

    def _process_player_death(self, player, cause):
        pass


class GameApp(App):
    """Main class of the application."""

    @staticmethod
    def _load_markup_files():
        project_directory = os.getcwd()
        for root, _, files in os.walk(project_directory):
            markup_files = [
                os.path.join(root, file_name)
                for file_name in files
                if file_name.endswith('.kv')]
            for file_name in markup_files:
                Builder.load_file(file_name)

    @staticmethod
    def _add_resources_folders():
        resource_add_path('biplanes/data')

    def build(self):
        """Should return main widget"""
        self._load_markup_files()
        self._add_resources_folders()
        return BiplanesClassicLevel().scene

if __name__ == "__main__":
    GameApp().run()
