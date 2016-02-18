import os.path

from kivy.lang import Builder

from biplanes.controllers.fire_button.fire_button import FireButton

dirrectory_path = os.path.dirname(os.path.realpath(__file__))

Builder.load_file(os.path.join(dirrectory_path, 'fire_button.kv'))
