import os.path

from functools import partial

from kivy.logger import Logger
from kivy.properties import ObjectProperty
from kivy.properties import BoundedNumericProperty
from kivy.properties import NumericProperty
from kivy.vector import Vector
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.resources import resource_add_path
from parabox.behaviour import Collidable
from parabox.behaviour import Movable
from parabox.phisics import PlainPhisics
from parabox.structures import ObjectsCollection
from parabox.structures import Collector

from biplanes import settings as global_settings
from biplanes.entities.bullet.bullet import Bullet
from biplanes.entities.plane import settings as plane_settings


current_directory = os.path.dirname(os.path.realpath(__file__))
resource_add_path(os.path.join(current_directory, 'data'))
Builder.load_file(os.path.join(current_directory, 'ground.kv'))


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
