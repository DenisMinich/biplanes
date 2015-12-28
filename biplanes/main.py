from kivy.app import App
from kivy.clock import Clock
from kivy.resources import resource_add_path
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.uix.widget import Widget
from parabox.base_object import BaseObject
from parabox.phisics import PlainPhisics
from parabox.structures import ObjectsCollection, Collector

from biplanes.entities import Plane
from biplanes.settings import STATIC_PATH

resource_add_path(STATIC_PATH)
Builder.load_file('game.kv')


class Battlefield(BaseObject):
    def __init__(self, *args, **kwargs):
        super(Battlefield, self).__init__(*args, **kwargs)
        self.objects = ObjectsCollection([
            Plane(
                size=(35, 35),
                pos=(500, 300),
                speed_limit=5,
                foreground='red_plane.png'),
            Plane(
                size=(35, 35),
                pos=(300, 300),
                speed_limit=5,
                foreground='blue_plane.png'),],
            self)
        self.phisics = ObjectsCollection([
            PlainPhisics(
                gravity=(1, -1),
                affect_objects=Collector.get_collection('planes'))],
            self)


class GameApp(App):
   def build(self):
       battlefield = Battlefield()
       Clock.schedule_interval(battlefield.update, 1./60)
       return battlefield

if __name__ == "__main__":
    GameApp().run()
