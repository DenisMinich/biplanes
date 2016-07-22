"""ControlBuilder implementation"""

from biplanes.controls.enums import Control
from biplanes.controls.exceptions import ControlBuilderError
from biplanes.controls.manual.manual import ManualControl


class ControlBuilder(object):  # pylint: disable=too-few-public-methods
    """Creates and returns contoller by scene name"""

    def __init__(self, control_owner):
        """Class constructor"""
        self._control_owner = control_owner

    def create_control(self, control_name):
        """Creates control by name

        :param scene_name: name of scene to create
        :type scene_name: str
        """
        if control_name == Control.PLAYER_CONTROL:
            manual_control = ManualControl()
            self._control_owner.controls.add(manual_control)
            return manual_control
        if control_name == Control.AI_BEGINNER:
            raise NotImplementedError('Beginner AI not implemented')
        else:
            raise ControlBuilderError("Unknown control name")
