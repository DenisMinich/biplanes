from kivy.vector import Vector
from kivy.uix.image import Image
from parabox.behaviour import Collidable
from parabox.behaviour import Movable
from parabox.structures.collector import Collector

from . import settings


class Bullet(Movable, Image, Collidable):
    def __init__(self, *args, **kwargs):
        self.owner = kwargs.get('owner', None)
        super(Bullet, self).__init__(
            size=(5, 5),
            pos=self._get_start_position(),
            velocity=self._get_start_velocity(),
            source='bullet.png')
        self.add_to_collections(['bullets'])
        self.add_to_collections(['game_objects'])
        self.bind(on_update=self._delete_on_out_from_scene)
        self.bind(on_collide=self._process_collissions)

    def _get_start_velocity(self):
        direction = Vector(1, 0).rotate(self.owner.angle).normalize()
        return direction * settings.BULLET_SPEED

    def _get_start_position(self):
        deviation = Vector(
            self.owner.width / 2, 0).rotate(self.owner.angle)
        return (
            self.owner.center_x + deviation.x,
            self.owner.center_y + deviation.y)

    def _delete_on_out_from_scene(self, instance):
        """Delete from all collections if position out of parent's borders
        """
        if ((self.x + self.size[0] > self.parent.size[0])
                or (self.x < 0)
                or (self.y + self.size[1] > self.parent.size[1])
                or (self.y < 0)):
            self.delete_from_collections()

    def _process_collissions(self, instance, collide_object):
        if collide_object in Collector.get_collection('planes'):
            collide_object.damage(1)
            self.delete_from_collections()
