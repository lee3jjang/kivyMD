from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
#:import MDListBottomSheet kivymd.uix.bottomsheet.MDListBottomSheet
#:import MDGridBottomSheet kivymd.uix.bottomsheet.MDGridBottomSheet
#:import toast kivymd.toast.toast

Screen:
    name: "MainScreen"

    MDToolbar:
        title: "Example"
        pos_hint: {"top": 1}
        elevation: 10

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
'''

class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        return Builder.load_string(KV)


Test().run()