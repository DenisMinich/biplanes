"""DefaultGun implementation"""

from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.resources import resource_find
from kivy.uix.image import Image
from kivy.vector import Vector

from biplanes.base_entity import BaseEntity
from biplanes.bullets.enums import BulletModel
from biplanes.bullets.factory import BulletFactory
from biplanes import enums as common_enums


class DefaultGun(BaseEntity):
    """Base plane gun widget"""

    texture = ObjectProperty()
    """Visual representation of the gun"""

    plane = ObjectProperty()
    """Planes assigned with this gun"""

    angle = NumericProperty(0)
    """Rotation angle"""

    max_bullet_instances = NumericProperty(3)
    """Max bullets for scene from this gun"""

    bullets_count = NumericProperty(0)
    """How many bullet exists on the scene from this gun"""

    cooldown = NumericProperty(10)
    """Timeout between shots in ticks"""

    ticks_to_prepare = NumericProperty(0)
    """How many ticks to wait until new shot"""

    direction = StringProperty(common_enums.Direction.RIGHT)
    """Direction of the gun"""

    @property
    def ready_to_shot(self):
        """Is gun ready for shot"""
        return not self.ticks_to_prepare

    def __init__(self, plane=None, *args, **kwargs):
        self.plane = plane
        super(DefaultGun, self).__init__(*args, **kwargs)
        texture = Image(
            source=resource_find('gun_default.png'), nocache=True).texture
        if self.direction == common_enums.Direction.LEFT:
            # pylint: disable=no-member
            texture.flip_vertical()
            # pylint: enable=no-member
        self.texture = texture

    def fire(self):
        """Creates bullet assigned for this gun"""
        if (self.ready_to_shot and
                self.bullets_count < self.max_bullet_instances):
            bullet = self._create_bullet()
            bullet.bind(on_delete=self._on_bullet_deleted)
            self.add_item(bullet)
            self.ticks_to_prepare = self.cooldown
            self.bullets_count += 1

    def update(self):
        super(DefaultGun, self).update()
        if not self.ready_to_shot:
            self.ticks_to_prepare -= 1

    def _create_bullet(self):
        """Creates instance of bullet"""
        plane_offset = 5  # used to prevent self-damaging exact after fire
        relative_mazzle_coords = (self.plane.size[0] / 2 + plane_offset, 0)
        center_to_muzzle_vector = Vector(relative_mazzle_coords).rotate(
            self.plane.angle)
        rotation_delta = (
            center_to_muzzle_vector[0] - relative_mazzle_coords[0],
            center_to_muzzle_vector[1] - relative_mazzle_coords[1])
        absolute_mazzle_coords = (
            self.plane.pos[0] + self.plane.size[0] + plane_offset,
            self.plane.pos[1] + self.plane.size[1] / 2)
        bullet_pos = (
            absolute_mazzle_coords[0] + rotation_delta[0],
            absolute_mazzle_coords[1] + rotation_delta[1])
        bullet = BulletFactory.get_bullet(
            BulletModel.DEFAULT, pos=bullet_pos, angle=self.plane.angle,
            team=self.plane.team, scene=self.plane.scene)
        return bullet

    def _on_bullet_deleted(self, _):
        self.bullets_count -= 1
