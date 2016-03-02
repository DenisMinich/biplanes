from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.resources import resource_add_path
from parabox.base_object import BaseObject
from parabox.phisics import PlainPhisics
from parabox.structures import Collector
from parabox.structures import ObjectsCollection

from biplanes.controllers import ClockWiseButton
from biplanes.controllers import ConterClockWiseButton
from biplanes.controllers import DownButton
from biplanes.controllers import FireButton
from biplanes.controllers import Info
from biplanes.controllers import UpButton
from biplanes.entities import Plane
from biplanes.settings import GLOBAL_GRAVITY
from biplanes.settings import STATIC_PATH


resource_add_path(STATIC_PATH)
Builder.load_file('game.kv')


class Battlefield(BaseObject):
    def __init__(self, *args, **kwargs):
        super(Battlefield, self).__init__(*args, **kwargs)
        self.blue_plane = Plane(
            id="Blue plane",
            start_pos=(40, 200),
            source='blue_plane.png')
        self.red_plane = Plane(
            id="Red plane",
            start_pos=(340, 200),
            source='red_plane.png')
        self.add_widget(UpButton(self.blue_plane))
        self.add_widget(DownButton(self.blue_plane))
        self.add_widget(ClockWiseButton(self.blue_plane))
        self.add_widget(ConterClockWiseButton(self.blue_plane))
        self.add_widget(FireButton(self.blue_plane))

    def on_touch_down(self, *args):
        if self.red_plane.points:
            self.red_plane.damage(1)


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
        shadow = BaseObject()
        shadow.objects = ObjectsCollection(
            Collector.get_collection('hidden_objects'),
            parent_widget=shadow)
        Clock.schedule_interval(battlefield.update, 1./60)
        Clock.schedule_interval(shadow.update, 1./60)
        return battlefield

if __name__ == "__main__":
    GameApp().run()
