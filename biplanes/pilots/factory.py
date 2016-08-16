"""PilotFactory implementation"""

from biplanes.pilots.default.default import DefaultPilot
from biplanes.pilots.enums import Pilot
from biplanes.pilots.exceptions import PilotFactoryError


class PilotFactory(object):  # pylint: disable=too-few-public-methods
    """Creates pilot by it's name"""

    @staticmethod
    def get_pilot(pilot_name):
        """Returns pilot widget by it's name

        :param pilot_name: name of pilot model to create
        :type pilot_name: str
        """
        if pilot_name == Pilot.DEFAULT_PILOT:
            return DefaultPilot()
        else:
            raise PilotFactoryError("Unknown pilot model name")
