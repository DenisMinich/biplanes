from kivy.uix.widget import Widget


class BaseButton(Widget):

    _target = None

    def assign(self, target):
        self._target = target

    def unassign(self):
        self._target = None
