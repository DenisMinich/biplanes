"""DecorFactory implementation"""

from biplanes.decors.airship.airship import Airship
from biplanes.decors.enums import DecorModel
from biplanes.decors.exceptions import DecorFactoryError
from biplanes.decors.explosion.explosion import Explosion
from biplanes.decors.ground.ground import Ground


class DecorFactory(object):  # pylint: disable=too-few-public-methods
    """Creates decors by decor name"""

    @staticmethod
    def get_decor(decor_name, *args, **kwargs):
        """Returns decor widget by it's name

        :param decor_name: name of decoration to create
        :type decor_name: str
        """
        if decor_name == DecorModel.EXPLOSION:
            return Explosion(*args, **kwargs)
        elif decor_name == DecorModel.GROUND:
            return Ground(*args, **kwargs)
        elif decor_name == DecorModel.AIRSHIP:
            return Airship(*args, **kwargs)
        else:
            raise DecorFactoryError("Unknown decor name")
