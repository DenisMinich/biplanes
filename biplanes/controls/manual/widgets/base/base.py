"""Base class for controller button"""

from kivy.uix.widget import Widget


class BaseButton(Widget):
    """Base controller class"""

    _target = None

    def _on_assign(self):
        """Actions before assign button"""
        pass

    def _on_unassign(self):
        """Actions before unassign button"""
        pass

    def assign(self, target):
        """Assign button with target plane

        :param target: plane to control by target
        :type target: biplanes.entities.plane.plane.Plane
        """
        self._on_assign()
        self._target = target

    def unassign(self):
        """Unassign button from target plane"""
        self._on_unassign()
        self._target = None

    def _touch_down(self):
        """Perform actions on touch down"""
        pass

    def _touch_up(self):
        """Perform actions on touch up"""
        pass

    def on_touch_down(self, touch):
        if self._target is not None:
            if self.collide_point(touch.x, touch.y):
                self._touch_down()

    def on_touch_up(self, touch):
        if self._target is not None:
            self._touch_up()
