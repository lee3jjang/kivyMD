from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import (
    ThreeLineAvatarIconListItem, IconLeftWidget, ImageLeftWidget, IRightBodyTouch
)
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.utils import get_color_from_hex

class RightCheckbox(IRightBodyTouch, MDCheckbox):
    pass

KV = '''
ScrollView:

    MDList:
        id: container
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        button = MDIconButton(
            icon="language-python",
            user_font_size="64sp",
            theme_text_color="Custom",
            text_color=self.theme_cls.primary_color,
            on_release=lambda btn: print(btn.icon)
        )
        # button.bind(on_release=lambda btn: print(btn.icon))
        self.root.ids.container.add_widget(button)
        for i in range(20):
            list_item = ThreeLineAvatarIconListItem(
                    text=f"Three-line item {i} with avatar",
                    secondary_text="Secondary text here",
                    tertiary_text= "fit more text than usual",
                )
            if i%3 == 0:
                list_item.add_widget(IconLeftWidget(icon="language-python"))
            elif i%3 == 1:
                list_item.add_widget(ImageLeftWidget(source='assets/images/stocks.png'))
            else:
                list_item.add_widget(IconLeftWidget(icon="plus"))
                list_item.add_widget(RightCheckbox())

            self.root.ids.container.add_widget(list_item)

MainApp().run()