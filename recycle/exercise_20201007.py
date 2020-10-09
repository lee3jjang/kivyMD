from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
ScreenManager:
    Screen:
        name: 'main'
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: "Drawer"
            MDFlatButton:
                text: "Ok"
                on_release:
                    root.current = 'notmain'
                    root.transition.direction = 'left'
            MDRectangleFlatButton:
                text: "Cancel"

    Screen:
        name: 'notmain'
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: "2nd Drawer"
            MDRectangleFlatButton:
                text: "test"
                on_release:
                    root.transition.direction = 'right'
                    root.current = 'main'
'''

class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        return Builder.load_string(KV)


Test().run()