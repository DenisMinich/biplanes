"""DefaultBullet implementation"""

from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.vector import Vector

from biplanes.base_entity import BaseEntity


class DefaultBullet(BaseEntity):
    """Base plane bullet widget"""

    texture = ObjectProperty()

    plane = ObjectProperty()

    scene = ObjectProperty()
    """Scene object"""

    angle = NumericProperty(0)
    """Rotation angle"""

    velocity = NumericProperty()
    """Actual velocity"""

    @property
    def velocity_vector(self):
        """Vector of plane's velocity"""
        return Vector(self.velocity, 0).rotate(self.angle)

    def __init__(self, *args, team=None, angle=None, scene=None, **kwargs):
        super(DefaultBullet, self).__init__(*args, **kwargs)
        self.texture = Image(source='bullet_default.png').texture
        self.size = (5, 5)
        self.velocity = 7
        self.scene = scene
        self.team = team
        self.angle = angle

    def update(self):
        """Update state of the plane"""
        self._move()
        self._check_in_scene()

    def _move(self):
        self.pos = (
            self.pos[0] + self.velocity_vector[0],
            self.pos[1] + self.velocity_vector[1])

    def _check_in_scene(self):
        in_scene = (0 < self.center_x < self.scene.size[0]) and \
            (0 < self.center_y < self.scene.size[1])
        if not in_scene:
            self.remove_item(self)
