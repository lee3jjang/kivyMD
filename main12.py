from kivymd.app import MDApp
from kivy.lang.builder import Builder

KV = '''
<MyTile@SmartTileWithStar>:
    size_hint_y: None
    height: "240dp"

ScrollView:

    MDGridLayout:
        cols: 3
        adaptive_height: True
        padding: dp(4), dp(4)
        spacing: dp(4)

        MyTile:
            stars: 5
            source: "colours.png"

        MyTile:
            stars: 2
            source: "colours2.png"

        MyTile:
            stars: 1
            source: "colours.png"
            text: "[size=26]Cat2[/size]\\n[size=16]Hello~[/size]"

        MyTile:
            stars: 3
            source: "colours2.png"

        MyTile:
            stars: 4
            source: "colours.png"

        MyTile:
            stars: 3
            source: "colours2.png"
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MyApp().run()