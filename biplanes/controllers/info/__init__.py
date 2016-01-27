import os.path

from kivy.lang import Builder

from biplanes.controllers.info.info import Info

dirrectory_path = os.path.dirname(os.path.realpath(__file__))

Builder.load_file(os.path.join(dirrectory_path, 'info.kv'))
