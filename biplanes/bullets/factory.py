"""BulletFactory implementation"""

from biplanes.bullets.default.default import DefaultBullet
from biplanes.bullets.enums import BulletModel
from biplanes.bullets.exceptions import BulletFactoryError


class BulletFactory(object):  # pylint: disable=too-few-public-methods
    """Creates bullet by it's name"""

    @staticmethod
    def get_bullet(bullet_name, *args, **kwargs):
        """Returns bullet widget by it's name

        :param bullet_name: name of bullet model to create
        :type bullet_name: str
        """
        if bullet_name == BulletModel.DEFAULT:
            return DefaultBullet(*args, **kwargs)
        else:
            raise BulletFactoryError("Unknown bullet model name")
