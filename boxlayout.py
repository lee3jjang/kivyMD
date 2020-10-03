from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton

KV = '''
        
'''


class Example(MDApp):
    
    def __init__(self):
        super().__init__()
        self.theme_cls.primary_palette = 'Teal'

    def build(self):
        layout = BoxLayout(
            orientation='vertical',
            size_hint=(None, None),
            pos_hint={'center_x': .5, 'center_y': .5},
        )

        btn1 = MDFlatButton(
            text="My Flat Button",
            font_size="18sp",
            size_hint=(None, None),
            pos_hint={'center_x': .5, 'center_y': .5},
        )

        btn2 = MDFlatButton(
            text="My Flat Button",
            font_size="18sp",
            size_hint=(None, None),
            pos_hint={'center_x': .5, 'center_y': .5},
        )

        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout

Example().run()