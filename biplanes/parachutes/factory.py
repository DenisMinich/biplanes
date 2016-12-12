"""ParachuteFactory implementation"""

from biplanes.parachutes.default import default
from biplanes.parachutes import enums
from biplanes.parachutes import exceptions


class Factory(object):  # pylint: disable=too-few-public-methods
    """Creates parachute by it's name"""

    @staticmethod
    def get(name, *args, **kwargs):
        """Returns parachute widget by it's name

        :param name: name of parachute model to create
        :type name: str
        """
        if name == enums.Model.DEFAULT:
            return default.DefaultParachute(*args, **kwargs)
        else:
            raise exceptions.ParachuteFactoryError(
                "Unknown parachute model name")
