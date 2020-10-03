from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
Screen:
    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: True
        icon: "android"
        right_pad: True
'''

class Example(MDApp):
    data = {
        'language-python': 'Python',
        'language-php': 'PHP',
        'language-cpp': 'C++',
    }

    def build(self):
        return Builder.load_string(KV)

Example().run()