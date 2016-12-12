"""BreakingEffect implementation"""
from biplanes.mechanic.affectable import effect


# pylint: disable=too-few-public-methods
class BreakingEffect(effect.Effect):
    """Effect limits maximum falling velocity of pilot"""

    binds = ['max_gravity_velocity']

    def __init__(self, *args, max_velocity, **kwargs):
        super(BreakingEffect, self).__init__(*args, **kwargs)
        self.max_velocity = max_velocity

    def max_gravity_velocity(self, attribute):
        """Overriding pilots max velocity"""
        return min(attribute, self.max_velocity)

    def __repr__(self):
        return "BreakingEffect(velocity={max_velocity!r})".format(
            max_velocity=self.max_velocity)


# pylint: disable=too-few-public-methods
class MovingEffect(effect.Effect):
    """Applies additional movement"""

    binds = ['velocity']

    def __init__(self, *args, velocity, **kwargs):
        super(MovingEffect, self).__init__(*args, **kwargs)
        self.effect_velocity = velocity

    def velocity(self, attribute):
        """Override target object's velocity"""
        return attribute + self.effect_velocity

    def __repr__(self):
        return "MovintEffect(velocity={velocity!r})".format(
            velocity=self.velocity)
