"""Main module of the app and contains main app class."""

import os

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy import properties
from kivy.resources import resource_add_path
from kivy.uix.widget import Widget

from biplanes.controls.enums import Control
from biplanes.controls.factory import ControlFactory
from biplanes.decors import enums as decors_enums
from biplanes.decors.factory import DecorFactory
from biplanes import enums as common_enums
from biplanes.guns.enums import GunModel
from biplanes.guns.factory import GunFactory
from biplanes.planes import enums as planes_enums
from biplanes.planes.factory import PlaneFactory
from biplanes.scenes import enums as scenes_enums
from biplanes.scenes.factory import SceneFactory
from biplanes.textures import enums as textures_enums
from biplanes.textures.factory import TextureFactory


class BiplanesClassicLevel(Widget):
    """Classic biplanes level"""

    _scene = None

    _update_interval = 1. / 40

    _objects_to_update = None

    _clock = None

    respawn_interval = 1

    blue_team = common_enums.BlueTeam

    red_team = common_enums.RedTeam

    score = properties.DictProperty({blue_team: 0, red_team: 0})

    @property
    def scene(self):
        """Scene property"""
        return self._scene

    def __init__(self):
        super(BiplanesClassicLevel, self).__init__()
        self._objects_to_update = set()
        self._create_scene()
        self._create_player_plane()
        self._create_ai_plane()
        self._start_level()

    def _start_level(self):
        """Setup update objects on schedule"""
        self._clock = Clock.schedule_interval(
            self._update_level, self._update_interval)

    def _update_level(self, *_):
        self._update_inner_objects()
        self._process_collissions()

    def _update_inner_objects(self):
        """Update inner objects"""
        for inner_object in self._objects_to_update.copy():
            inner_object.update()

    def _process_collissions(self):
        """Search for items' collissions and process them"""
        level_objects = list(self._objects_to_update)
        for index, inner_object in enumerate(level_objects):
            for another_object in level_objects[index:]:
                if inner_object.collide_widget(another_object):
                    inner_object.process_collission(another_object)
                    another_object.process_collission(inner_object)

    def on_item_added(self, _, item):
        """Callback on new item added"""
        self.add_item(item)

    def on_item_removed(self, _, item):
        """Callback on item removed"""
        self.remove_item(item)

    def add_item(self, item):
        """Add item to the scene"""
        self._scene.add_widget(item)
        self._objects_to_update.add(item)
        item.bind(on_add_item=self.on_item_added)
        item.bind(on_remove_item=self.on_item_removed)

    def remove_item(self, item):
        """Remove item from the scene"""
        self._scene.remove_widget(item)
        self._objects_to_update.remove(item)
        item.unbind(on_add_item=self.on_item_added)
        item.unbind(on_remove_item=self.on_item_removed)

    def _create_scene(self):
        self._scene = SceneFactory.get_scene(
            scenes_enums.Scene.BIPLANES_CLASSIC)
        self._scene.size = (800, 600)
        self.add_item(DecorFactory.get_decor(
            decors_enums.DecorModel.BARN, pos=(325, 40), size=(150, 100)))
        self.add_item(DecorFactory.get_decor(
            decors_enums.DecorModel.GROUND, scene=self._scene))
        self.add_item(DecorFactory.get_decor(
            decors_enums.DecorModel.AIRSHIP, scene=self._scene, level=self))
        self.add_item(DecorFactory.get_decor(
            decors_enums.DecorModel.CLOUD, size=(250, 180), angle=-180,
            flight_height_middle=self.scene.height * .7,
            flight_height_dispersion=self.scene.height * .1,
            left_border=-150, right_border=950))
        self.add_item(DecorFactory.get_decor(
            decors_enums.DecorModel.CLOUD, size=(250, 180), angle=-180,
            flight_height_middle=self.scene.height * .7,
            flight_height_dispersion=self.scene.height * .1,
            left_border=-150, right_border=950))

    def _create_player_plane(self, *_):
        textures_pack = TextureFactory.get_textures_pack(
            textures_enums.TexturePackModel.BLUE_PLANE)
        blue_plane = PlaneFactory.get_plane(
            planes_enums.PlaneModel.STANDART, scene=self.scene, pos=(20, 42),
            textures=textures_pack, direction=common_enums.Direction.RIGHT)
        blue_plane.team = self.blue_team
        blue_plane.bind(on_destroy=self._process_player_plane_destroyed)
        blue_plane.bind(on_ejection=self._process_player_plane_ejected)
        blue_plane.control = ControlFactory.get_control(
            Control.PLAYER_CONTROL)
        blue_plane.gun = GunFactory.get_gun(GunModel.DEFAULT, plane=blue_plane)
        self.add_item(blue_plane)
        self.add_item(blue_plane.control)
        self.add_item(blue_plane.gun)

    def _process_player_plane_destroyed(self, plane, cause):
        self.remove_item(plane.control)
        self.remove_item(plane.gun)
        if plane.is_contains_pilot:
            if cause == plane.DEATH_DAMAGED:
                self.score[self.red_team] += 1
            elif cause == plane.DEATH_CRASH:
                self.score[self.blue_team] -= 1
            Clock.schedule_once(
                self._create_player_plane, self.respawn_interval)

    def _process_player_plane_ejected(self, plane, pilot):
        self.remove_item(plane.control)
        plane.control = ControlFactory.get_control(Control.AUTOPILOT)
        pilot.control = ControlFactory.get_control(
            Control.PLAYER_PILOT_CONTROL)
        pilot.bind(on_kill=self._process_player_pilot_killed)
        pilot.bind(on_achieve=self._process_player_achieved_spawn)
        self.add_item(pilot.control)

    def _process_player_pilot_killed(self, pilot, cause):
        self.remove_item(pilot)
        self.remove_item(pilot.control)
        if cause:
            pass

    def _process_player_achieved_spawn(self, pilot):
        self.remove_item(pilot)
        self.remove_item(pilot.control)
        self._create_player_plane()

    def _create_ai_plane(self, *_):
        textures_pack = TextureFactory.get_textures_pack(
            textures_enums.TexturePackModel.RED_PLANE)
        red_plane = PlaneFactory.get_plane(
            planes_enums.PlaneModel.STANDART, scene=self.scene, pos=(725, 42),
            textures=textures_pack, direction=common_enums.Direction.LEFT)
        red_plane.bind(on_destroy=self._process_ai_plane_destroyed)
        red_plane.team = self.red_team
        red_plane.control = ControlFactory.get_control(Control.AI_BEGINNER)
        red_plane.gun = GunFactory.get_gun(
            GunModel.DEFAULT, plane=red_plane,
            direction=common_enums.Direction.LEFT)
        self.add_item(red_plane)
        self.add_item(red_plane.control)
        self.add_item(red_plane.gun)

    def _process_ai_plane_destroyed(self, plane, cause):
        self.remove_item(plane.control)
        self.remove_item(plane.gun)
        if plane.is_contains_pilot:
            if cause == plane.DEATH_DAMAGED:
                self.score[self.blue_team] += 1
            elif cause == plane.DEATH_CRASH:
                self.score[self.red_team] -= 1
            Clock.schedule_once(
                self._create_ai_plane, self.respawn_interval)


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
