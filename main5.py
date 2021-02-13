
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivy.properties import StringProperty, ListProperty

KV = '''
Screen:
    MDBoxLayout:
        orientation: 'vertical'

        MyButton:
            icon: "android"
            colour: 0, 1, 0, .2

        MyButton:
            icon: "language-python"
            colour: 0, 0, 1, .2

<MyButton>:
    canvas:
        Color:
            rgba: root.colour
        Rectangle:
            pos: self.pos
            size: self.size
    theme_text_color: "Custom"
    text_color: app.theme_cls.primary_color
    pos_hint: {"center_x": .5, "center_y": .5}     
'''

class MyButton(MDIconButton):
    colour = ListProperty()

    def on_release(self):
        print(self.icon)

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()