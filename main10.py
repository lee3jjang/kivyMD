from kivymd.app import MDApp
from kivy.lang.builder import Builder

KV = '''
MDChooseChip:

    MDChip:
        text: 'Earth'
        icon: 'earth'
        selected_chip_color: .21176470535294, .098039627451, 1, 1

    MDChip:
        text: 'Face'
        icon: 'face'
        selected_chip_color: .21176470535294, .098039627451, 1, 1

    MDChip:
        text: 'Facebook'
        icon: 'facebook'
        selected_chip_color: .21176470535294, .098039627451, 1, 1
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def do_something(self):
        print("Do Something!")

MyApp().run()