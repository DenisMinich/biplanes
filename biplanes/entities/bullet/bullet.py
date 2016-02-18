from kivy.vector import Vector
from parabox.behaviour import Movable
from parabox.visual import ImageView

from . import settings


class Bullet(Movable, ImageView):
    def __init__(self, *args, **kwargs):
        self.owner = kwargs.get('owner', None)
        super(Bullet, self).__init__(
            size=(5, 5),
            pos=self._get_start_position(),
            velocity=self._get_start_velocity(),
            foreground='bullet.png')
        self.add_to_collections(['bullets'])
        self.bind(on_update=self._delete_on_out_from_scene)

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



