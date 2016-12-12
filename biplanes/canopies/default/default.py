"""DefaultCanopy implementation"""
from biplanes import base_entity
from biplanes.canopies import effects as canopy_effects

from kivy import properties
from kivy import resources
from kivy.uix import image
from kivy import vector


# pylint: disable=too-many-ancestors
# pylint: disable=too-many-instance-attributes
class DefaultCanopy(base_entity.BaseEntity):
    """Default parachute's canopy widget"""

    pilot = properties.ObjectProperty(None, allownone=True)

    texture = properties.ObjectProperty(None, allownone=True)

    is_tilted_left = properties.BooleanProperty(False)

    is_tilted_right = properties.BooleanProperty(False)

    tags = properties.ListProperty(["canopy"])

    def __init__(self, *args, pilot, **kwargs):
        super(DefaultCanopy, self).__init__(*args, **kwargs)
        self.pilot = pilot
        self.size = (50, 30)
        self.texture = image.Image(
            source=resources.resource_find(
                'canopy.png')
        ).texture
        self._init_effects()
        self.bind(is_tilted_left=self._tilt_left)
        self.bind(is_tilted_right=self._tilt_right)
        self._apply_canopy_effect()
        self.bind(on_delete=self._remove_canopy_effect)

    def _init_effects(self):
        self.breaking_effect = canopy_effects.BreakingEffect(max_velocity=2)
        self.tilt_left_effect = canopy_effects.MovingEffect(
            velocity=vector.Vector(-1, 0))
        self.tilt_right_effect = canopy_effects.MovingEffect(
            velocity=vector.Vector(1, 0))

    def _tilt_left(self, _, value):
        if value:
            self.pilot.add_effect(self.tilt_left_effect)
        else:
            self.pilot.remove_effect(self.tilt_left_effect)

    def _tilt_right(self, _, value):
        if value:
            self.pilot.add_effect(self.tilt_right_effect)
        else:
            self.pilot.remove_effect(self.tilt_right_effect)

    def _apply_canopy_effect(self):
        self.pilot.add_effect(self.breaking_effect)

    def _remove_canopy_effect(self, *_):
        self.pilot.remove_effect(self.breaking_effect)

    def update(self):
        super(DefaultCanopy, self).update()
        self._update_pos()

    def _update_pos(self):
        self.x = self.pilot.center_x - self.size[0] / 2
        self.y = self.pilot.y + self.pilot.size[1]
