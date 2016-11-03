"""Standart biplane implementation"""

from kivy import properties
from kivy import vector

from biplanes.decors import enums as decors_enums
from biplanes.decors.factory import DecorFactory
from biplanes import enums as common_enums
from biplanes.pilots import enums as pilots_enums
from biplanes.pilots.factory import PilotFactory
from biplanes.planes.base.base import BasePlane


# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-ancestors
class StandartPlane(BasePlane):
    """Standart biplane"""

    texture_on_start = properties.ObjectProperty()

    texture_normal = properties.ObjectProperty()

    texture_damaged = properties.ObjectProperty()

    texture_critical_damaged = properties.ObjectProperty()

    scene = properties.ObjectProperty()

    direction = properties.StringProperty(common_enums.Direction.RIGHT)

    def __init__(
            self, *args, scene=None, textures=None, direction=None, **kwargs):
        super(StandartPlane, self).__init__(*args, **kwargs)
        self.scene = scene
        self.direction = direction
        self._apply_textures(textures)
        self.angle = 0 if direction == common_enums.Direction.RIGHT else 180
        self.takeoff_point = 4
        self.max_velocity = 5
        self.ejection_velocity = 6
        self.max_points = 3
        self.points = 3
        self.acceleration = .15
        self.braking = .15
        self.rotate_clockwise_velocity = 3
        self.rotate_conterclockwise_velocity = 3
        self.size = (50, 50)
        self.register_event_type('on_ejection')

    def _apply_textures(self, textures):
        """Assign textures for the plane"""
        self.texture_on_start = textures.plane_on_start
        self.texture_normal = textures.plane_normal
        self.texture_damaged = textures.plane_damaged
        self.texture_critical_damaged = textures.plane_critical_damaged
        if self.direction == common_enums.Direction.LEFT:
            # pylint: disable=no-member
            self.texture_on_start.flip_vertical()
            self.texture_normal.flip_vertical()
            self.texture_damaged.flip_vertical()
            self.texture_critical_damaged.flip_vertical()
            # pylint: enable=no-member

    def update(self):
        super(StandartPlane, self).update()
        self._return_to_scene()

    def eject(self):
        """Catapult pilot"""
        if self.is_contains_pilot:
            pilot = PilotFactory.get_pilot(pilots_enums.PilotModel.DEFAULT)
            pilot.angle = self.angle + 90
            pilot.velocity = self.ejection_velocity
            pilot.center_x, pilot.y = self._get_ejected_pilot_position()
            self.add_item(pilot)
            self.dispatch('on_ejection', pilot)
        self.is_contains_pilot = False

    def destroy(self, cause):
        explosion = DecorFactory.get_decor(
            decors_enums.DecorModel.EXPLOSION, center=self.center)
        self.add_item(explosion)
        super(StandartPlane, self).destroy(cause)

    def on_ejection(self, pilot):
        """Method should be called if pilot was ejected"""
        pass

    def on_points(self, _, value):
        """Update planes state based on current points"""
        if value == 3 and self.is_in_air:
            self.texture = self.texture_on_start
        elif value == 3 and not self.is_in_air:
            self.texture = self.texture_normal
        elif value == 2:
            self.texture = self.texture_damaged
        elif value == 1:
            self.texture = self.texture_critical_damaged

    def _return_to_scene(self):
        plane_length = self.size[0]
        scene_length = self.scene.size[0]
        if self.center_x > scene_length:
            self.pos[0] = -plane_length / 2
        if self.center_x < 0:
            self.pos[0] = scene_length - plane_length / 2

    def _get_ejected_pilot_position(self):
        relative_cabin_coords = (0, self.size[1] / 2)
        center_to_cabin_vector = vector.Vector(relative_cabin_coords).rotate(
            self.angle)
        rotation_delta = (
            center_to_cabin_vector[0] - relative_cabin_coords[0],
            center_to_cabin_vector[1] - relative_cabin_coords[1])
        absolute_cabin_coords = (
            self.pos[0] + self.size[0] / 2,
            self.pos[1] + self.size[1])
        pilot_pos = (
            absolute_cabin_coords[0] + rotation_delta[0],
            absolute_cabin_coords[1] + rotation_delta[1])
        return pilot_pos

    def process_collission(self, item):
        if item.has_tags("solid"):
            self.destroy(self.DEATH_CRASH)
