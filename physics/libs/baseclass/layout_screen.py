from kivy.uix.label import Label
from kivy.uix.image import Image

class RootWidget(Label):

    def do_layout(self, *args):
        number_of_children = len(self.children)
        width = self.width
        width_per_child = width // number_of_children

        positions = range(0, width, width_per_child)
        for position, child in zip(positions, self.children):
            child.height = self.height
            child.x = self.x + position
            child.y = self.y
            child.width = width_per_child

    def on_size(self, *args):
        self.do_layout()

    def on_pos(self, *args):
        self.do_layout()

    def add_widget(self, widget):
        super(RootWidget, self).add_widget(widget)
        self.do_layout()

    def remove_widget(self, widget):
        super(RootWidget, self).remove_widget(widget)
        self.do_layout()