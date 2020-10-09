from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import ListProperty, StringProperty
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp

KV = '''
<Root@BoxLayout>
    orientation: 'vertical'
    
    MDChip:
        label: 'Coffee'
        color: .4470588235118, .1960787254902, 0, 1
        icon: 'coffee'
        check: True

<MyLabel>
    halign: 'center'
'''

class MyLabel(MDLabel):
    pass

class Test(MDApp):
    def build(self):
        Builder.load_string(KV)
        self.screen = Factory.Root()
        self.screen.add_widget(MyLabel(text="Hello Screen"))
        return self.screen


Test().run()