from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.behaviors import RectangularElevationBehavior, FocusBehavior, HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior

Window.size = (960, 1009)
Window.position = 'custom'
Window.left, Window.top = (960, -1049)

KV = """
MDScreen:
    
    MDBoxLayout:
        id: box
        pos_hint: {'center_x': .5, 'center_y': .5}
        size_hint: .8, .8
        md_bg_color: app.theme_cls.bg_darkest
"""

class HoverItem(MDBoxLayout, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.md_bg_color = (1, 1, 1, 1)

    def on_leave(self):
        self.md_bg_color = self.theme_cls.bg_darkest

class Test(MDApp):
    def build(self):
        self.screen = Builder.load_string(KV)
        for _ in range(5):
            self.screen.ids.box.add_widget(HoverItem())
        return self.screen

Test().run()