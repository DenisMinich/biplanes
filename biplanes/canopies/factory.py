"""Factory implementation"""

from biplanes.canopies.default import default
from biplanes.canopies import enums
from biplanes.canopies import exceptions


class Factory(object):  # pylint: disable=too-few-public-methods
    """Creates canopy by it's name"""

    @staticmethod
    def get(name, *args, **kwargs):
        """Returns canopy widget by it's name

        :param name: name of canopy model to create
        :type name: str
        """
        if name == enums.Model.DEFAULT:
            return default.DefaultCanopy(*args, **kwargs)
        else:
            raise exceptions.CanopyFactoryError("Unknown canopy model name")
