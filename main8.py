from kivymd.app import MDApp
from kivy.lang.builder import Builder

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDBottomAppBar:
        md_bg_color: 0, 1, 0, 1

        MDToolbar:
            title: "MDToolbar"
            icon: "git"
            type: "bottom"
            mode: "free-end"
            left_action_items: [["menu", lambda x: print("Hello World!")]]
            icon_color: 0, 1, 0, 1
            on_action_button:
                print("Action Button Clicked!")
'''


class Main(MDApp):
    def build(self):
        return Builder.load_string(KV)

Main().run()