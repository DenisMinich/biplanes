"""Plane builder implementation"""

from biplanes.planes.enums import PlaneModel
from biplanes.planes.exceptions import PlaneBuilderError
from biplanes.planes.standart.standart import StandartPlane


class PlaneBuilder(object):  # pylint: disable=too-few-public-methods
    """Creates plane by its model's name"""

    def __init__(self, plane_owner):
        """Class constructor"""
        self._plane_owner = plane_owner

    def create_plane(self, team, model, control):
        """Creates plane

        :param team: plane's team
        :type team: str
        :param model: plane's model
        :param model: str
        :type control: plane's control
        :type control: biplanes.controls.base.base.BaseControl
        """
        if model == PlaneModel.STANDART:
            plane = StandartPlane()
        else:
            raise PlaneBuilderError("Unknown plane's model name")
        plane.scene = self._plane_owner
        plane.team = team
        plane.control = control
        self._plane_owner.planes.add(plane)
        return plane
