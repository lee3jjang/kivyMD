from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

import random

class ScatterTextWidget(BoxLayout):
    text_colour = ObjectProperty([1, 0, 0, 1])

    def change_label_colour(self, *args):
        colour = [random.random() for _ in range(3)] + [1]
        label = self.ids.my_label
        label.color = colour