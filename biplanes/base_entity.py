"""BaseEntity implementation"""

from biplanes.tags.tagable import Tagable


class BaseEntity(Tagable):
    """Base class for item on scene

    Main purpose: be sure that every object on level has 2 basic events:
        'on_add_item' if item adds new item for the scene
        'on_remove_item' if item removes item from the scene
    """

    def __init__(self, *args, **kwargs):
        super(BaseEntity, self).__init__(*args, **kwargs)
        self.register_event_type('on_add_item')
        self.register_event_type('on_remove_item')
        self.register_event_type('on_delete')

    def add_item(self, item):
        """Add new item to scene"""
        self.dispatch('on_add_item', item)

    @staticmethod
    def on_add_item(item):
        """Method should be called if class adds new scene's item"""
        pass

    def remove_item(self, item):
        """Delete item from scene"""
        self.dispatch('on_remove_item', item)

    @staticmethod
    def on_remove_item(item):
        """Method should be called for remove class from scene"""
        item.dispatch('on_delete')

    def update(self):
        """Update state of entity in time"""
        pass

    def on_delete(self):
        """Method called if entity should be removed"""
        pass

    def process_collission(self, item):
        """Process collision of entity with item"""
        pass
