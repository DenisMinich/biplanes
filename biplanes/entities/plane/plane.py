from parabox.behaviour import Movable
from parabox.visual import ImageView


class Plane(Movable, ImageView):
    def __init__(self, *args, **kwargs):
        super(Plane, self).__init__(*args, **kwargs)
        self.add_to_collections(['planes'])
