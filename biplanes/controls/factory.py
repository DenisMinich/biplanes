"""ControlFactory implementation"""

from biplanes.controls.enums import Control
from biplanes.controls.exceptions import ControlFactoryError
from biplanes.controls.manual.manual import ManualControl


class ControlFactory(object):  # pylint: disable=too-few-public-methods
    """Creates and returns contoller by scene name"""

    @staticmethod
    def get_control(control_name):
        """Creates control by name

        :param scene_name: name of scene to create
        :type scene_name: str
        """
        if control_name == Control.PLAYER_CONTROL:
            manual_control = ManualControl()
            return manual_control
        if control_name == Control.AI_BEGINNER:
            raise NotImplementedError('Beginner AI not implemented')
        else:
            raise ControlFactoryError("Unknown control name")
