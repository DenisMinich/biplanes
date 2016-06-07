from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.properties import ObjectProperty
from kivy.resources import resource_add_path
from kivy.uix.image import Image
from parabox.base_object import BaseObject
from parabox.phisics import PlainPhisics
from parabox.structures import Collector
from parabox.structures import ObjectsCollection

from biplanes.controllers.manual import ManualControl
from biplanes.entities import Plane
from biplanes.entities.blue_plane.blue_plane import BluePlane
from biplanes.entities.ground import Ground
from biplanes.settings import GLOBAL_GRAVITY
from biplanes.settings import STATIC_PATH


resource_add_path(STATIC_PATH)
Builder.load_file('game.kv')


class Battlefield(BaseObject):

    texuture = ObjectProperty()

    def __init__(self, *args, **kwargs):
        self.texture = Image(source='background.png').texture
        super(Battlefield, self).__init__(*args, **kwargs)
        self.blue_plane = BluePlane(
            id="Blue plane", source='blue_plane.png')
        game_controller = ManualControl()
        self.blue_plane.controller = game_controller
        self.add_widget(game_controller)
        Ground(pos=(0, 0), size=(800, 40))


class GameApp(App):

    def build(self):
        battlefield = Battlefield()
        battlefield.phisics = ObjectsCollection([
            PlainPhisics(
                gravity=(0, -GLOBAL_GRAVITY),
                affect_objects=Collector.get_collection('planes'))],
            parent_widget=battlefield)
        battlefield.objects = ObjectsCollection(
            Collector.get_collection('game_objects'),
            parent_widget=battlefield)
        battlefield.environment = ObjectsCollection(
            Collector.get_collection('environment'),
            parent_widget=battlefield)
        shadow = BaseObject()
        shadow.objects = ObjectsCollection(
            Collector.get_collection('hidden_objects'),
            parent_widget=shadow)
        Clock.schedule_interval(battlefield.update, 1./60)
        Clock.schedule_interval(shadow.update, 1./60)
        return battlefield

if __name__ == "__main__":
    GameApp().run()
