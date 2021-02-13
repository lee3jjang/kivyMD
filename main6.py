
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivymd.icon_definitions import md_icons

KV = '''
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "Example Tabs"

    MDTabs:        
        id: tabs
        on_tab_switch: print("Hello Switch")

<MyTab>:

    MDIconButton:
        id: icon
        icon: app.icons[0]
        user_font_size: "48sp"
        pos_hint: {"center_x": .5, "center_y": .5}
'''

class MyTab(FloatLayout, MDTabsBase):
    pass

class Test(MDApp):
    icons = list(md_icons.keys())[15:30]

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for name_tab in self.icons:
            self.root.ids.tabs.add_widget(MyTab(text=name_tab))

Test().run()

git config --global user.email "you@example.com"
git config --global user.name "Your Name"