"""DefaultParachute implementation"""
from biplanes import base_entity
from biplanes.canopies import enums as canopy_enums
from biplanes.canopies import factory as canopy_factory

from kivy import properties


# pylint: disable=too-many-ancestors
# pylint: disable=too-many-instance-attributes
class DefaultParachute(base_entity.BaseEntity):
    """Default parachute widget"""

    canopy = properties.ObjectProperty(None, allownone=True)

    texture = properties.ObjectProperty(None, allownone=True)

    tags = properties.ListProperty(["parachute"])

    def __init__(self, *args, pilot, **kwargs):
        super(DefaultParachute, self).__init__(*args, **kwargs)
        self.pilot = pilot
        self.is_used = False
        self.pilot.bind(on_landed=self.cut_canopy)

    def pull_the_ring(self):
        """Executes ring action"""
        if not self.is_used:
            self.canopy = canopy_factory.Factory.get(
                canopy_enums.Model.DEFAULT, pilot=self.pilot)
            self.add_item(self.canopy)
            self.is_used = True
        elif self.canopy is not None:
            self.cut_canopy()

    def cut_canopy(self, *_):
        """Сut canopy from the parachute"""
        if self.canopy is not None:
            self.remove_item(self.canopy)
            self.canopy = None
