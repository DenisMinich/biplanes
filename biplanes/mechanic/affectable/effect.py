"""Effect implementation"""
from kivy import properties

from biplanes.mechanic.affectable import affectable


# pylint: disable=too-few-public-methods
class Effect(affectable.Affectable):
    """Base class for each effect"""

    binds = properties.ListProperty([])
