from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineIconListItem

Window.size = (960, 1009)
Window.position = 'custom'
Window.left, Window.top = (960, -1049)

KV = """
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)

        MDBoxLayout:
            adaptive_height: True

            MDIconButton:
                icon: 'magnify'

            MDTextField:
                id: search_field
                hint_text: 'Search icon'
        
        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'
            
            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'

<CustomOneLineIconListItem>:

    IconLeftWidget:
        icon: root.icon
"""

class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()

class Test(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)

    def on_start(self):
        self.root.ids.rv.data = []
        for name_icon in md_icons.keys():
            self.root.ids.rv.data.append({
                "viewclass": "CustomOneLineIconListItem",
                "icon": name_icon,
                "text": name_icon,
                "callback": lambda x: x,
            })
        self.fps_monitor_start()

Test().run()