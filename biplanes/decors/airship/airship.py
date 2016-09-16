"""Airship implementation"""

from random import random

from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.vector import Vector

from biplanes.base_entity import BaseEntity


# pylint: disable=too-many-instance-attributes
class Airship(BaseEntity):
    """Airship with total level score decoration"""

    texture = ObjectProperty()
    """Self texture"""

    level = ObjectProperty()
    """Level object"""

    scene = ObjectProperty()
    """Scene object"""

    angle = NumericProperty(0)
    """Rotation angle"""

    velocity = NumericProperty()
    """Actual velocity"""

    height_factor = NumericProperty()
    """How high aircraft in it's corridor"""

    height_middle = NumericProperty()
    """Center of travel corridor"""

    height_dispersion = NumericProperty()
    """How much aircraft's height may change"""

    score_text = StringProperty()
    """Score text"""

    @property
    def velocity_vector(self):
        """Vector of velocity"""
        return Vector(self.velocity, 0).rotate(self.angle)

    def __init__(self, *args, level=None, scene=None, **kwargs):
        self.level = level
        self.scene = scene
        self.texture = Image(source='airship.png').texture
        super(Airship, self).__init__(*args, **kwargs)
        self.scene.bind(size=self._callback_scene_size_changed)
        self.level.bind(score=self._callback_score_changed)
        self.angle = 0
        self.velocity = .3
        self.size = (200, 100)
        self._next_height_factor()
        self._update_position()
        self._update_score_text()

    def update(self):
        self._move()
        self._return_to_scene()

    def _move(self):
        self.pos = (
            self.pos[0] + self.velocity_vector[0],
            self.pos[1] + self.velocity_vector[1])

    def _return_to_scene(self):
        if self.x > self.scene.width:
            self.x = -self.width
            self._next_height_factor()
            self.center_y = self._get_height()

    def _get_height(self):
        """Randoms new height in available range"""
        corridor_height = self.height_dispersion * 2
        corridor_lower_point = self.height_middle - self.height_dispersion
        return self.height_factor * corridor_height + corridor_lower_point

    def _next_height_factor(self):
        """Randoms height factor"""
        self.height_factor = random()

    def _get_team_text(self, team):
        return "[color={color}]{score}[/color]".format(
            color=team.color, score=self.level.score[team])

    @staticmethod
    def _get_delimeter_text():
        return "[color=000000] : [/color]"

    def _update_score_text(self):
        """Rebuild score text"""
        self.score_text = self._get_delimeter_text().join(
            self._get_team_text(team) for team in self.level.score)

    def _update_position(self):
        """Recalculate airship's position"""
        self.height_middle = self.scene.height * .7
        self.height_dispersion = self.scene.height * .1
        self.center_x = self.scene.center_x
        self.center_y = self._get_height()

    def _callback_scene_size_changed(self, *_):
        self._update_position()

    def _callback_score_changed(self, *_):
        self._update_score_text()
