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
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

Window.size = 144*3, 256*3

KV = '''
FloatLayout:
    MDFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_alert_dialog()
'''

class Example(MDApp):
    title = 'Hello My App!'
    dialog = None

    def __init__(self):
        super().__init__()
        self.theme_cls.primary_palette = 'Teal'

    def build(self):
        return Builder.load_string(KV)

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = "Dialog Title",
                text = "This will reset your device to its default factory settings.",
                size_hint = (0.8, None),
                buttons = [
                    MDFlatButton(text="CANCEL", text_color=self.theme_cls.primary_color),
                    MDFlatButton(text="DISCARD", text_color=self.theme_cls.primary_color),
                ]
            )
        self.dialog.open()

app = Example()
app.run()