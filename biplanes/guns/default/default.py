"""DefaultGun implementation"""

from kivy.properties import ObjectProperty
from kivy.resources import resource_find
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.vector import Vector

from biplanes.bullets.enums import BulletModel
from biplanes.bullets.factory import BulletFactory


class DefaultGun(Widget):
    """Base plane gun widget"""

    _texture = ObjectProperty()

    _plane = ObjectProperty()

    def __init__(self, plane=None, *args, **kwargs):
        self._plane = plane
        super(DefaultGun, self).__init__(*args, **kwargs)
        self._texture = Image(source=resource_find('gun_default.png')).texture

    def fire(self):
        """Creates bullet assigned for this gun"""
        bullet_pos_x = self._plane.pos[0] + self._plane.size[0]
        bullet_pos_y = self._plane.pos[1] + self._plane.size[1] / 2
        bullet_source_vector = Vector(
            self._plane.size[0], self._plane.size[1] / 2)
        bullet_source_vector = bullet_source_vector.rotate(self._plane.angle)
        bullet_pos = (
            bullet_pos_x + bullet_source_vector[0],
            bullet_pos_y + bullet_source_vector[1])
        bullet = BulletFactory.get_bullet(
            BulletModel.DEFAULT, pos=bullet_pos, angle=self._plane.angle,
            source=self._plane)
        self.dispatch('on_create', bullet)
