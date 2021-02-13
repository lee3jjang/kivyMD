import os
from pathlib import Path

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

Window.size = (960, 1009)
Window.position = 'custom'
Window.left, Window.top = (960, -1049)

os.environ["PHYSICS_ROOT"] = str(Path(__file__).parent)
KV_DIR = f"{os.environ['PHYSICS_ROOT']}/libs/kv/"

for kv_file in os.listdir(KV_DIR):
    with open(os.path.join(KV_DIR, kv_file), encoding="utf-8") as kv:
        Builder.load_string(kv.read())

# KV = """
# #:import ScatterTextWidget libs.baseclass.root_screen.ScatterTextWidget

# ScatterTextWidget:
# """

# KV = """
# #:import ScrollableLabel libs.baseclass.scroll_screen.ScrollableLabel

# ScrollableLabel:
# """

KV = """
#:import RootWidget libs.baseclass.layout_screen.RootWidget

RootWidget:
"""

class TutorialApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Physics"

    def build(self):
        return Builder.load_string(KV)
        
TutorialApp().run()