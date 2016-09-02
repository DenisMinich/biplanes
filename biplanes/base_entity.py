"""BaseEntity implementation"""

from kivy.uix.widget import Widget


class BaseEntity(Widget):
    """Base class for item on scene"""

    def __init__(self, *args, **kwargs):
        super(BaseEntity, self).__init__(*args, **kwargs)
        self.register_event_type('on_create_item')
        self.register_event_type('on_remove_item')

    def create_item(self, item):
        """Add new item to scene"""
        self.dispatch('on_create_item', item)

    def remove_item(self, item):
        """Delete item from scene"""
        self.dispatch('on_remove_item', item)

    @staticmethod
    def on_create_item(item):
        """Method should be called if class creates new scene's item"""
        pass

    @staticmethod
    def on_remove_item(item):
        """Method should be called for remove class from scene"""
        pass
