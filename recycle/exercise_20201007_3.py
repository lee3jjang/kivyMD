from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
Window.size = (300, 500)

KV = '''
Screen:
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "280dp", "180dp"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            text: "Title"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]

        MDSeparator:
            height: "1dp"

        MDLabel:
            text: "Body"

    MDFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5}
        on_release: app.show_dialog()
'''


class Test(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)

    def show_dialog(self):
        self.dialog = MDDialog(
            text="Discard draft?",
            buttons=[
                MDFlatButton(text="CANCEL", text_color=self.theme_cls.primary_color),
                MDFlatButton(text="DISCARD", text_color=self.theme_cls.primary_color),
            ],
        )
        self.dialog.open()

Test().run()