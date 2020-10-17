from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.factory import Factory
Window.size = (144*3, 256*3)

KV = '''
<MyTile@SmartTileWithLabel>
    size_hint_y: None
    # height: "240dp"

ScrollView:
    MDGridLayout:
        cols: 3
        adaptive_height: True
        padding: dp(4), dp(4)
        spacing: dp(4)

        MyTile:
            text: "[size=26][color=#ffffff]Cat 1[/color][/size]\\n[size=14]cat-1.jfif[/size]"
            source: 'images/cat1.jfif'
        MyTile:
            stars: 5
            source: 'images/cat2.jfif'
        MyTile:
            stars: 5
            source: 'images/cat3.jfif'
        MyTile:
            stars: 5
            source: 'images/cat4.jfif'
        MyTile:
            stars: 5
            source: 'images/cat5.jfif'
        MyTile:
            stars: 5
            source: 'images/cat6.jfif'
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        pass

MyApp().run()