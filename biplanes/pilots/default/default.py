"""DefaultPilot implementation"""

from biplanes.mechanic.movable import movable

from kivy.properties import ObjectProperty
from kivy.uix.image import Image


# pylint: disable=too-few-public-methods
# pylint: disable=too-many-ancestors
class DefaultPilot(movable.Movable):
    """Base pilot widget"""

    _texture = ObjectProperty()

    @property
    def control(self):
        """Property for control"""
        return self._control

    @control.setter
    def control(self, value):
        if self._control is not None:
            self._control.unassign()
        self._control = value
        self._control.assign(self)

    _control = ObjectProperty()
    """Control of a plane"""

    def __init__(self):
        self._texture = Image(source='pilot.png').texture
        super(DefaultPilot, self).__init__()

    def update(self):
        self.move()
