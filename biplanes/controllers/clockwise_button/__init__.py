import os.path

from kivy.lang import Builder

from biplanes.controllers.clockwise_button.clockwise_button import ClockWiseButton

dirrectory_path = os.path.dirname(os.path.realpath(__file__))

Builder.load_file(os.path.join(dirrectory_path, 'clockwise_button.kv'))
