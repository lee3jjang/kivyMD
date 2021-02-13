from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

from kivy.properties import ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import time
import random

Window.size = (960, 1009)
Window.position = 'custom'
Window.left, Window.top = (960, -1049)

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ColourScreen(Screen):
    colour = ListProperty([1., 0., 0., 1.])

class MyScreenManager(ScreenManager):
    def new_colour_screen(self):
        name = str(time.time())
        s = ColourScreen(name=name, colour=[random.random() for _ in range(3)] + [1.])
        self.add_widget(s)
        self.current = name

first_screen = """
<FirstScreen>:
    name: 'first'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'first screen!'
            font_size: 30
        Image:
            source: 'colours.png'
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            Button:
                text: 'goto second screen'
                font_size: 30
                on_release: app.root.current = 'second'
            Button:
                text: 'goto random colour screen'
                font_size: 30
                on_release: app.root.new_colour_screen()
"""

second_screen = """
<SecondScreen>:
    name: 'second'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'second screen!'
            font_size: 30
        Image:
            source: 'colours2.png'
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            Button:
                text: 'goto first screen'
                font_size: 30
                on_release: app.root.current = 'first'
            Button:
                text: 'goto random colour screen'
                font_size: 30
                on_release: app.root.new_colour_screen()
"""

colour_screen = """
<ColourScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'colour {:.2},{:.2},{:.2} screen'.format(*root.colour[:3])
            font_size: 30
        Widget:
            canvas:
                Color:
                    rgba: root.colour
                Ellipse:
                    pos: self.pos
                    size: self.size
        BoxLayout:
            Button:
                text: 'goto first screen'
                font_size: 30
                on_release: app.root.current = 'first'
            Button:
                text: 'get random colour screen'
                font_size: 30
                on_release: app.root.new_colour_screen()
"""

KV = """
#:import FadeTransition kivy.uix.screenmanager.FadeTransition

MyScreenManager:
    transition: FadeTransition()
    FirstScreen:
    SecondScreen:
"""

class TutorialApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Physics"

    def build(self):
        Builder.load_string(first_screen)
        Builder.load_string(second_screen)
        Builder.load_string(colour_screen)
        return Builder.load_string(KV)
        
TutorialApp().run()