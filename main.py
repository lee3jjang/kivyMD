from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
Window.size = (144*3, 256*3)

class MyApp(MDApp):
    def build(self):
        return Builder.load_file('libs/kv/start_screen.kv')

if __name__ == '__main__':
    MyApp().run()

