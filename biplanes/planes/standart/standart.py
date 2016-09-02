"""Standart biplane implementation"""

from kivy.properties import ObjectProperty
from kivy.resources import resource_find
from kivy.uix.image import Image

from biplanes.guns.enums import GunModel
from biplanes.guns.factory import GunFactory
from biplanes.planes.base.base import BasePlane


# pylint: disable=too-many-instance-attributes
class StandartPlane(BasePlane):
    """Standart biplane"""

    _texture_on_start = ObjectProperty()

    _texture_normal = ObjectProperty()

    _texture_damaged = ObjectProperty()

    _texture_critical_damaged = ObjectProperty()

    _scene = ObjectProperty()

    def __init__(self, scene):
        super(StandartPlane, self).__init__()
        self._scene = scene
        self._texture_on_start = Image(
            source=resource_find('blue_plane.png')).texture
        self._texture_normal = Image(
            source=resource_find('blue_plane.png')).texture
        self._texture_damaged = Image(
            source=resource_find('blue_plane.png')).texture
        self._texture_critical_damaged = Image(
            source=resource_find('blue_plane.png')).texture
        self.takeoff_point = 4
        self.max_velocity = 5
        self.max_points = 3
        self.points = 3
        self.is_in_air = False
        self.is_in_move = False
        self.acceleration = .03
        self.braking = .03
        self.rotate_clockwise_velocity = 3
        self.rotate_conterclockwise_velocity = 3
        self.size = (50, 50)
        self.pos = (20, 42)
        self.gun = GunFactory.get_gun(GunModel.DEFAULT, plane=self)
        self.create_item(self.gun)

    def _return_to_scene(self):
        plane_length = self.size[0]
        scene_length = self._scene.size[0]
        if self.center_x > scene_length:
            self.pos[0] = -plane_length / 2
        if self.center_x < 0:
            self.pos[0] = scene_length - plane_length / 2

    def update(self):
        super(StandartPlane, self).update()
        self._return_to_scene()

    def on_points(self, _, value):
        """Update planes state based on current points"""
        if value == 3 and self.is_in_air:
            self.texture = self._texture_on_start
        elif value == 3 and not self.is_in_air:
            self.texture = self._texture_normal
        elif value == 2:
            self.texture = self._texture_damaged
        elif value == 1:
            self.texture = self._texture_critical_damaged
