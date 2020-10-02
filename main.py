import os
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.font_definitions import theme_font_styles
from kivy.core.text import LabelBase

KV = '''
Screen:

    MDLabel:
        text: "JetBrainsMono"
        halign: "center"
'''

class MainApp(MDApp):
    title = 'My Main Title'
    
    def build(self):
        # primary_palette, primary_hue
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        
        return Builder.load_string(KV)


app = MainApp()
app.run()