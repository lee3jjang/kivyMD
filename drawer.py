# from kivy.lang import Builder
# from kivy.factory import Factory
# from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
# from kivymd.uix.button import MDFlatButton
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider
from kivymd.uix.list import OneLineIconListItem, MDList, IconLeftWidget
from kivymd.uix.navigationdrawer import NavigationLayout, MDNavigationDrawer

Window.size = 144*3, 256*3

KV = '''
<ItemDrawer>
    theme_text_color: "Custom"
    
    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: .5, .7, .2, 1
'''

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    

class DrawerList(ThemableBehavior, MDList):
    pass

class Example(MDApp):
    title = 'Hello My App!'

    def __init__(self):
        super().__init__()
        self.theme_cls.primary_palette = 'Teal'

    def build(self):
        Builder.load_string(KV)
        layout = MDBoxLayout(orientation='vertical', padding="10dp")

        # Label
        label1 = MDLabel(text="KivyMD library", font_style="Button", size_hint_y= None)
        label2 = MDLabel(text="kivydevelopment@gmail.com", font_style="Caption", size_hint_y= None)
        layout.add_widget(label1)
        layout.add_widget(label2)


        # Scroll View
        scrollview = ScrollView()
        layout.add_widget(scrollview)
        self.md_list = DrawerList()
        scrollview.add_widget(self.md_list)
        

        return layout

    def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }

        for icon_name in icons_item.keys():
            self.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )
        for icon_name in icons_item.keys():
            self.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )

app = Example()
app.run()