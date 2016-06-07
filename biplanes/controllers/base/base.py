from parabox.base_object import BaseObject


class BaseControl(BaseObject):

    _target = None

    def assign(self, target):
        self._target = target

    def unassign(self):
        self._target = None
