from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex
from kivy.properties import ListProperty, StringProperty

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.color_definitions import colors

KV = '''
<Root@BoxLayout>
    orientation: 'vertical'

    MDToolbar:
        title: app.title

    MDTabs:
        id: android_tabs
        on_tab_switch: app.on_tab_switch(*args)
        size_hint_y: None
        height: "48dp"
        tab_indicator_anim: True

    ScrollView:

        MDList:
            id: box

<ItemColor>:
    size_hint_y: None
    height: "20dp"

    canvas:
        Color:
            rgba: root.color # root=ItemColor의 instance
        
        Rectangle:
            size: self.size
            pos: self.pos

    MDLabel:
        text: root.text
        halign: "center"

<Tab>:
'''

class Tab(BoxLayout, MDTabsBase):
    pass

class ItemColor(BoxLayout):
    text = StringProperty()
    color = ListProperty()

class MainApp(MDApp):
    title = 'This is My Application'
    
    def build(self):
        # # primary_palette, primary_hue
        # self.theme_cls.primary_palette = 'Purple'
        # self.theme_cls.primary_hue = "500"
        # self.theme_cls.theme_style = "Light"

        Builder.load_string(KV)
        self.screen = Factory.Root()

        # Tabs에 colors의 key를 이름으로 하는 Tab 추가
        # Tab : MDTabsBase를 상속 받음
        for name_tab in colors.keys():
            self.screen.ids.android_tabs.add_widget(Tab(text=name_tab))
        return self.screen

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tabs_label, tab_text):
        self.screen.ids.box.clear_widgets()
        for value_color in colors[tab_text]:
            self.screen.ids.box.add_widget(
                ItemColor(
                    color = get_color_from_hex(colors[tab_text][value_color]),
                    text = value_color,
                )
            )

    def on_start(self):
        self.on_tab_switch(None, None, None, self.screen.ids.android_tabs.ids.layout.children[-1].text)

app = MainApp()
app.run()