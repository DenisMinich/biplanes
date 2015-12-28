from kivy.app import App
from kivy.clock import Clock
from kivy.resources import resource_add_path
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.uix.widget import Widget
from parabox.base_object import BaseObject
from parabox.structures import ObjectsCollection

from biplanes.entities import Plane
from biplanes.settings import STATIC_PATH

resource_add_path(STATIC_PATH)
Builder.load_file('game.kv')


class Battlefield(BaseObject):
    def __init__(self, *args, **kwargs):
        super(Battlefield, self).__init__(*args, **kwargs)
        self.objects = ObjectsCollection([
            Plane(size=(35, 35), pos=(500, 300), foreground='red_plane.png'),
            Plane(size=(35, 35), pos=(300, 300), foreground='blue_plane.png'),],
            self)

class GameApp(App):
   def build(self):
       battlefield = Battlefield()
       Clock.schedule_interval(battlefield.update, 1./60)
       return battlefield

if __name__ == "__main__":
    GameApp().run()
