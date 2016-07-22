"""BaseControl implementation"""

from parabox.base_object import BaseObject


class BaseControl(BaseObject):
    """Base implementation of control"""

    _target = None

    def assign(self, target):
        """Assign control to target plane"""
        self._target = target

    def unassign(self):
        """Unassign control from a plane"""
        self._target = None
