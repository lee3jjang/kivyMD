from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.factory import Factory
from kivymd.uix.behaviors import RectangularElevationBehavior, FocusBehavior, TouchBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDFloatingActionButton
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine, MDExpansionPanelThreeLine
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.menu import MDDropdownMenu
from kivymd import images_path
import os
import glob
Window.size = (144*3, 256*3)

start_screen = '''
Screen:
    MDRaisedButton:
        id: button
        text: 'PRESS ME'
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.menu.open()
'''

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Teal"

    def build(self):
        self.screen = Builder.load_string(start_screen)
        menu_items = [{'text': f'Item {i}'} for i in range(5)]
        self.menu = MDDropdownMenu(
            caller = self.screen.ids.button,
            items = menu_items,
            width_mult=4,
        )
        self.menu.bind(on_release=self.menu_callback)
        return self.screen

    def menu_callback(self, instance_menu, instance_menu_item):
        print(instance_menu, instance_menu_item)

if __name__ == '__main__':
    MyApp().run()