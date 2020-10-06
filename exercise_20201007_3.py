from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.card import MDCardSwipe
from kivy.properties import StringProperty
Window.size = (300, 500)

KV = '''
<SwipeToDeleteItem>
    size_hint_y: None
    height: content.height

    MDCardSwipeLayerBox:

    MDCardSwipeFrontBox:

        OneLineListItem:
            id: content
            text: root.text
            _no_ripple_effect: True

Screen:
    BoxLayout:
        orientation: "vertical"
        spacing: "10dp"

        MDToolbar:
            elevation: 10
            title: "MDCardSwipe"

        ScrollView:
            MDList:
                id: md_list
                padding: 0

'''
class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()

class Test(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(20):
            self.root.ids.md_list.add_widget(
                SwipeToDeleteItem(text=f"One-line item {i}")
            )

Test().run()