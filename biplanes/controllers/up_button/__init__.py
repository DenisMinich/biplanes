import os.path

from kivy.lang import Builder

from biplanes.controllers.up_button.up_button import UpButton

dirrectory_path = os.path.dirname(os.path.realpath(__file__))

Builder.load_file(os.path.join(dirrectory_path, 'up_button.kv'))
