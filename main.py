import os
import sys
from pathlib import Path

from kivy.core.window import Window
from kivy.loader import Loader
from kivy.lang import Builder

from kivymd.app import MDApp


# from libs.baseclass.list_items import KitchenSinkOneLineLeftIconItem

# os.environ 설정
os.environ['KIVY_PROFILE_LANG'] = '1'
sys.path.append(os.path.abspath(__file__).split('demos')[0])
os.environ['KITCHEN_SINK_ROOT'] = str(Path(__file__).parent)
os.environ['KITCHEN_SINK_ASSETS'] = os.path.join(
    os.environ['KITCHEN_SINK_ROOT'], f'assets{os.sep}'
)

Window.softinput_mode = 'below_target' # 뭔지 모르겠음

class KitchenSinkApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = 'Blue'
        self.dialog_change_theme = None
        self.toolbar = None
        self.data_screens = {}

    def build(self): 
        Builder.load_file(
            f"{os.path.join(os.environ['KITCHEN_SINK_ROOT'], 'libs', 'kv', 'list_items.kv')}"
        )

        return Builder.load_file(
            f"{os.path.join(os.environ['KITCHEN_SINK_ROOT'], 'libs', 'kv', 'start_screen.kv')}"
        )

KitchenSinkApp().run()
print("---end---")