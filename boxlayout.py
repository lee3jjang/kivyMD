from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color

Window.size = (300, 100)

class MyFlatButton(MDFlatButton):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flag = True

    def on_release(self):
        if self.flag:
            # self.canvas.clear()
            self.text = ''
        else:
            with self.canvas:
                Color(1, 0, 0, .5, mode='rgba')
                self.rect = Rectangle(pos=(80, 0), size=(140, 40))
                self.text = "Hello My Button!"
        self.flag = not self.flag


class Example(MDApp):
    title = 'Hello My App!'

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

        btn2 = MyFlatButton(
            text="My Flat Button",
            font_size="18sp",
            size_hint=(None, None),
            pos_hint={'center_x': .5, 'center_y': .5},
        )

        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout

app = Example()
app.run()