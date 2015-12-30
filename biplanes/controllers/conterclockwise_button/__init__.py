import os.path

from kivy.lang import Builder

from biplanes.controllers.conterclockwise_button.conterclockwise_button import (
	ConterClockWiseButton)

dirrectory_path = os.path.dirname(os.path.realpath(__file__))

Builder.load_file(os.path.join(dirrectory_path, 'conterclockwise_button.kv'))
