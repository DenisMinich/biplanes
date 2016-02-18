import os.path

from kivy.resources import resource_add_path


dirrectory_path = os.path.dirname(os.path.realpath(__file__))
resource_add_path(os.path.join(dirrectory_path, 'data'))
