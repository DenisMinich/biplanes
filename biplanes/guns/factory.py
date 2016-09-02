"""GunFactory implementation"""

from biplanes.guns.default.default import DefaultGun
from biplanes.guns.enums import GunModel
from biplanes.guns.exceptions import GunFactoryError


class GunFactory(object):  # pylint: disable=too-few-public-methods
    """Creates gun by it's name"""

    @staticmethod
    def get_gun(gun_name, *args, **kwargs):
        """Returns gun widget by it's name

        :param gun_name: name of gun model to create
        :type gun_name: str
        """
        if gun_name == GunModel.DEFAULT:
            return DefaultGun(*args, **kwargs)
        else:
            raise GunFactoryError("Unknown gun model name")
