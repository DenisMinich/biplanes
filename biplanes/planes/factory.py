"""PlaneFactory implementation"""

from biplanes.planes.enums import PlaneModel
from biplanes.planes.exceptions import PlaneFactoryError
from biplanes.planes.standart.standart import StandartPlane


class PlaneFactory(object):  # pylint: disable=too-few-public-methods
    """Creates plane by its model's name"""

    @staticmethod
    def get_plane(model, *args, **kwargs):
        """Creates plane

        :param model: plane's model
        :param model: str
        :type control: plane's control
        :type control: biplanes.controls.base.base.BaseControl
        """
        if model == PlaneModel.STANDART:
            return StandartPlane(*args, **kwargs)
        else:
            raise PlaneFactoryError("Unknown plane's model name")
