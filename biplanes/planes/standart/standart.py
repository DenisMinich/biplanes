"""Standart biplane implementation"""

from kivy.properties import ObjectProperty
from kivy.resources import resource_find
from kivy.uix.image import Image

from biplanes.pilots import enums as pilots_enums
from biplanes.pilots.factory import PilotFactory
from biplanes.planes.base.base import BasePlane


# pylint: disable=too-many-instance-attributes
class StandartPlane(BasePlane):
    """Standart biplane"""

    texuture_on_start = ObjectProperty()

    texuture_normal = ObjectProperty()

    texuture_damaged = ObjectProperty()

    texuture_critical_damaged = ObjectProperty()

    scene = ObjectProperty()

    def __init__(self, scene):
        super(StandartPlane, self).__init__()
        self.scene = scene
        self.texuture_on_start = Image(
            source=resource_find('blue_plane.png')).texture
        self.texuture_normal = Image(
            source=resource_find('blue_plane.png')).texture
        self.texuture_damaged = Image(
            source=resource_find('blue_plane.png')).texture
        self.texuture_critical_damaged = Image(
            source=resource_find('blue_plane.png')).texture
        self.takeoff_point = 4
        self.max_velocity = 5
        self.max_points = 3
        self.points = 3
        self.acceleration = .03
        self.braking = .03
        self.rotate_clockwise_velocity = 3
        self.rotate_conterclockwise_velocity = 3
        self.size = (50, 50)
        self.pos = (20, 42)
        self.register_event_type('on_ejection')

    def update(self):
        super(StandartPlane, self).update()
        self._return_to_scene()

    def eject(self):
        """Catapult pilot"""
        if self.is_contains_pilot:
            pilot = PilotFactory.get_pilot(pilots_enums.PilotModel.DEFAULT)
            self.add_item(pilot)
            self.dispatch('on_ejection', pilot)
        self.is_contains_pilot = False

    def on_ejection(self, pilot):
        """Method should be called if pilot was ejected"""
        pass

    def on_points(self, _, value):
        """Update planes state based on current points"""
        if value == 3 and self.is_in_air:
            self.texture = self.texuture_on_start
        elif value == 3 and not self.is_in_air:
            self.texture = self.texuture_normal
        elif value == 2:
            self.texture = self.texuture_damaged
        elif value == 1:
            self.texture = self.texuture_critical_damaged

    def _return_to_scene(self):
        plane_length = self.size[0]
        scene_length = self.scene.size[0]
        if self.center_x > scene_length:
            self.pos[0] = -plane_length / 2
        if self.center_x < 0:
            self.pos[0] = scene_length - plane_length / 2

    def process_collission(self, item):
        from biplanes.scenes.decorations.ground.ground import Ground
        if isinstance(item, Ground):
            self.destroy(self.DEATH_CRASH)
