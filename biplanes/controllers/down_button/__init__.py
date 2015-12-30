import os.path

from kivy.lang import Builder

from biplanes.controllers.down_button.down_button import DownButton

dirrectory_path = os.path.dirname(os.path.realpath(__file__))

Builder.load_file(os.path.join(dirrectory_path, 'down_button.kv'))
