import os
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    title = 'My Main Title'
    def build(self):
        return MDLabel(text="Hello", halign="center")

MainApp().run()