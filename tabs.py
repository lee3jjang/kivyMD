from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons

KV = '''
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "Example Tabs"

    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch(*args)

<Tab>
    MDIconButton:
        id: icon
        icon: app.icons[0]
        user_font_size: "48sp"
        pos_hint: {"center_x": .5, "center_y": .5}
        
'''

class Tab(FloatLayout, MDTabsBase):
    pass

class Example(MDApp):
    icons = list(md_icons.keys())[15:30]

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for name_tab in self.icons:
            self.root.ids.tabs.add_widget(Tab(text=name_tab))

    def on_tab_switch(self, inst_tabs, inst_tab, inst_tab_label, tab_text):
        count_icon = [k for k, v in md_icons.items() if v == tab_text]
        inst_tab.ids.icon.icon = count_icon[0]

app = Example()
app.run()
