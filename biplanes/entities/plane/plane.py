from parabox.behaviour import Movable
from parabox.phisics import PlainPhisics
from parabox.structures import ObjectsCollection
from parabox.visual import ImageView


class Plane(Movable, ImageView):
    def __init__(self, *args, **kwargs):
        super(Plane, self).__init__(*args, **kwargs)
        self.add_to_collections(['planes'])
        self.engine = PlainPhisics(gravity=(0, 0), affect_objects=[self])
        self.inner_phisics = ObjectsCollection([self.engine], self)
        self.bind(on_move=self._return_to_scene)
        self.bind(on_update=self.restrict_power)
        self.bind(on_update=self.rotate_engine)

    def rotate_engine(self, *args):
        self.engine.angle = self.angle

    def restrict_power(self, *args):
        if self.engine.gravity.x > 1:
            self.engine.gravity.x = 1
        if self.engine.gravity.x < 0:
            self.engine.gravity.x = 0

    def _return_to_scene(self, *args, **kwargs):
        if self.x + self.size[0] > self.parent.size[0]:
            self.pos[0] = 0
        if self.x < 0:
            self.pos[0] = self.parent.size[0] - self.size[0]
        if self.y + self.size[1] > self.parent.size[1]:
            self.pos[1] = 0
        if self.y < 0:
            self.pos[1] = self.parent.size[1] - self.size[1]
