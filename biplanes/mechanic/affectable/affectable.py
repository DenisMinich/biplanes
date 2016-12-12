"""Affectable implmenetation"""
from kivy import properties

from kivy import event


class Affectable(event.EventDispatcher):
    """Allows to override behaviour of class with effects"""

    effects = properties.DictProperty({})

    def __init__(self, *args, **kwargs):
        super(Affectable, self).__init__(*args, **kwargs)

    def add_effect(self, effect):
        """Apply effect on object"""
        for bind in effect.binds:
            self.effects.setdefault(bind, set()).add(effect)

    def remove_effect(self, effect):
        """Remove effect from object"""
        for bind in effect.binds:
            self.effects[bind].remove(effect)

    def __getattribute__(self, attribute_name):
        attribute = super(Affectable, self).__getattribute__(attribute_name)
        try:
            effects = super(Affectable, self).__getattribute__('effects')
        except AttributeError:
            effects = {}
        if attribute_name in effects:
            for effect in effects[attribute_name]:
                handler = getattr(effect, attribute_name)
                attribute = handler(attribute)
        return attribute
