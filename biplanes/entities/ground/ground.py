from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from parabox.behaviour import Collidable


class Ground(Collidable):

    texture = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super(Ground, self).__init__(*args, **kwargs)
        self.add_to_collections(['environment'])
        self.add_to_collections(['solid'])
        self.texture = Image(source='ground.png').texture
        self.texture.wrap = 'repeat'
        self.texture.uvsize = (8, 1)

    def __repr__(self):
        return "<Ground id='%s'>" % self.id
