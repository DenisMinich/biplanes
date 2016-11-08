"""ControlFactory implementation"""

from biplanes.controls.ai_beginner import ai_beginner
from biplanes.controls.autopilot import autopilot
from biplanes.controls.enums import Control
from biplanes.controls.exceptions import ControlFactoryError
from biplanes.controls.manual import manual
from biplanes.controls.manual_pilot import manual_pilot
from biplanes.controls.manual_runner import manual_runner


class ControlFactory(object):  # pylint: disable=too-few-public-methods
    """Creates and returns contoller by scene name"""

    @staticmethod
    def get_control(control_name):
        """Creates control by name

        :param scene_name: name of scene to create
        :type scene_name: str
        """
        if control_name == Control.PLAYER_CONTROL:
            return manual.ManualControl()
        if control_name == Control.PLAYER_PILOT_CONTROL:
            return manual_pilot.ManualPilotControl()
        if control_name == Control.PLAYER_RUNNER_CONTROL:
            return manual_runner.ManualRunnerControl()
        if control_name == Control.AI_BEGINNER:
            return ai_beginner.AIBeginner()
        if control_name == Control.AUTOPILOT:
            return autopilot.Autopilot()
        else:
            raise ControlFactoryError("Unknown control name")
