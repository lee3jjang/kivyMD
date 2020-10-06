from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = (300, 500)

KV = '''
#:import MDListBottomSheet kivymd.uix.bottomsheet.MDListBottomSheet
#:import MDGridBottomSheet kivymd.uix.bottomsheet.MDGridBottomSheet
#:import toast kivymd.toast.toast

Screen:
    name: "MainScreen"

    BoxLayout:
        orientation: "vertical"
        
        MDToolbar:
            title: "Example"
            pos_hint: {"top": 1}
            left_action_items: [["menu", lambda x: print(x)]]
            elevation: 10

        MDTabs:
            id: tabs

            MDTabsBase:
                text: "Tab 1"
            MDTabsBase:
                text: "Tab 2"
            MDTabsBase:
                text: "Tab 3"
            MDTabsBase:
                text: "Tab 4"
            MDTabsBase:
                text: "Tab 5"

        MDRaisedButton:
            text: "Open list bottom sheet"
            on_release:
                bottom_sheet_menu = MDGridBottomSheet()
                bottom_sheet_menu.add_item("Standard Item", lambda x: toast("youtube"), icon_src="youtube")
                bottom_sheet_menu.open()
                print(self)
                print(app)
                print(root)
            pos_hint: {"center_x": .5, "center_y": .5}

        MDTextField:
            hint_text: "This is hint text"
'''

class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        return Builder.load_string(KV)


Test().run()