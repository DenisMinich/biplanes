from kivy.properties import AliasProperty, BooleanProperty
from parabox.base_object import BaseObject

from biplanes.controllers.manual.widgets.base import BaseButton


class Info(BaseObject, BaseButton):

    def get_text(self):
        text = "Object: %s\n\n" % self._target.id
        for field in self.fields:
            steps = field.split('.')
            value = self._target
            for step in filter(bool, steps):
                value = getattr(value, step, None)
            text += "%s - %s\n" % (field, value)
        return text

    def set_text(self, value):
        self.text = value

    tick = BooleanProperty()

    text = AliasProperty(get_text, set_text, rebind=True, bind=['tick'])

    def __init__(self, *args, fields=None, **kwargs):
        self.fields = fields
        super(Info, self).__init__(*args, **kwargs)
        self.bind(on_update=self.update_text)

    def update_text(self, *args):
        self.tick = not self.tick
