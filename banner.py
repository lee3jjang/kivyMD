# from kivy.lang import Builder
# from kivy.factory import Factory
# from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.factory import Factory

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
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons

Window.size = 144*3, 256*3

class Tab(FloatLayout, MDTabsBase):
    pass

KV = '''
Screen:
    MDBanner:
        id: mybanner
        type: "two-line"
        text: ["One line string text example without actions.", "Two line string text example without actions."]
        over_widget: screen
        vertical_pad: toolbar.height

    MDToolbar:
        id: toolbar
        title: "Example Banners"
        elevation: 10
        pos_hint: {'top': 1}

    BoxLayout:
        id: screen
        orientation: "vertical"
        size_hint_y: None
        height: Window.height - toolbar.height

        OneLineListItem:
            text: "Banner without actions"
            on_release: mybanner.show()

        Widget:
'''

class Example(MDApp):
    title = 'Hello My App!'

    def __init__(self):
        super().__init__()
        self.theme_cls.primary_palette = 'Teal'

    def build(self):
        return Builder.load_string(KV)

app = Example()
app.run()