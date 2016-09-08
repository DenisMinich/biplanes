"""BaseControl implementation"""

from biplanes.base_entity import BaseEntity


class BaseControl(BaseEntity):
    """Base implementation of control"""

    _target = None

    def assign(self, target):
        """Assign control to target plane"""
        self._target = target

    def unassign(self):
        """Unassign control from a plane"""
        self._target = None
