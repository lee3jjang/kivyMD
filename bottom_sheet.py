from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider
from kivymd.toast import toast
from kivymd.uix.list import OneLineIconListItem, MDList, IconLeftWidget
from kivymd.uix.navigationdrawer import NavigationLayout, MDNavigationDrawer
from kivymd.uix.bottomsheet import MDListBottomSheet, MDGridBottomSheet

Window.size = 144*3, 256*3

KV = '''
Screen:
    MDToolbar:
        title: "Example BottomSheet"
        pos_hint: {"top": 1}
        elevation: 10

    MDRaisedButton:
        text: "Open list bottom sheet"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.show_list()

'''


class Example(MDApp):
    title = 'Hello My App!'

    def __init__(self):
        super().__init__()
        self.theme_cls.primary_palette = 'Blue'

    def build(self):
        return Builder.load_string(KV)

    def show_list(self):
        bottom_sheet_menu = MDGridBottomSheet()

        data = {
            "Facebook": "facebook",
            "YouTube": "youtube",
            "Twitter": "twitter",
            "Da Cloud": "cloud-upload",
            "Camera": "camera",
        }

        for name, icon in data.items():
            bottom_sheet_menu.add_item(
                name,
                lambda x, y=name: self.callback_for_menu(y),
                icon_src=icon
            )
        bottom_sheet_menu.open()
        
    def callback_for_menu(self, *args):
        toast(args[0])

app = Example()
app.run()