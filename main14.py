from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.lang.builder import Builder

KV = '''
MDSlider:
    min: 0
    max: 100
    value: 40
    on_active:
        print(self.value)
'''

class MyApp(MDApp):
    def build(self):
        
        return Builder.load_string(KV)

MyApp().run()