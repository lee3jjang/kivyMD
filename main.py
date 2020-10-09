# from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp

class MyApp(MDApp):
    def build(self):
        return Builder.load_file('libs/kv/start_screen.kv')

MyApp().run()