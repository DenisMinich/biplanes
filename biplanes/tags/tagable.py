"""Tagable implementation"""

from kivy.properties import ListProperty
from kivy.uix.widget import Widget

from biplanes.tags.tags import Tag


class Tagable(Widget):
    """Mixin adds to class tags functionality"""

    tags = ListProperty([])

    old_tags = ListProperty([])

    def __init__(self, *args, **kwargs):
        super(Tagable, self).__init__(*args, **kwargs)
        for tag in self.tags:
            Tag.add_tag(self, tag)
        self.old_tags = self.tags

    @staticmethod
    def on_tags(instance, new_tags):
        """Update tags collection in case objects changed tags"""
        for tag_to_remove in instance.old_tags - new_tags:
            Tag.remove_tag(instance, tag_to_remove)

        for tag_to_add in new_tags - instance.old_tags:
            Tag.add_tag(instance, tag_to_add)

    def has_tags(self, *tags):
        """Check if specidied tags assigned for object"""
        return set(tags) <= set(self.tags)
