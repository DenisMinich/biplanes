from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.resources import resource_add_path
from parabox.base_object import BaseObject
from parabox.phisics import PlainPhisics
from parabox.structures import Collector
from parabox.structures import ObjectsCollection

from biplanes.controllers import ClockWiseButton
from biplanes.controllers import ConterClockWiseButton
from biplanes.controllers import DownButton
from biplanes.controllers import UpButton
from biplanes.entities import Plane
from biplanes.settings import STATIC_PATH


resource_add_path(STATIC_PATH)
Builder.load_file('game.kv')


class Battlefield(BaseObject):
    def __init__(self, *args, **kwargs):
        super(Battlefield, self).__init__(*args, **kwargs)
        self.red_plane = Plane(
            size=(35, 35),
            pos=(500, 300),
            speed_limit=5,
            foreground='red_plane.png')
        self.blue_plane = Plane(
            size=(35, 35),
            pos=(300, 300),
            speed_limit=5,
            foreground='blue_plane.png')
        self.objects = ObjectsCollection([
            self.red_plane, self.blue_plane],
            parent_widget=self)
        self.phisics = ObjectsCollection([
            PlainPhisics(
                gravity=(0, -.5),
                affect_objects=Collector.get_collection('planes'))],
            self)
        self.add_widget(UpButton(self.blue_plane))
        self.add_widget(DownButton(self.blue_plane))
        self.add_widget(ClockWiseButton(self.blue_plane))
        self.add_widget(ConterClockWiseButton(self.blue_plane))


class GameApp(App):
    def build(self):
        battlefield = Battlefield()
        Clock.schedule_interval(battlefield.update, 1./60)
        return battlefield

if __name__ == "__main__":
    GameApp().run()
