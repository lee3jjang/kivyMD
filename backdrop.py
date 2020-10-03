from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp

Builder.load_string(
'''
#:import Window kivy.core.window.Window
#:import images_path kivymd.images_path
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget

<ItemBackdropFrontLayer@TwoLineAvatarListItem>
    icon: "android"

    IconLeftWidget:
        icon: root.icon

<MyBackdropBackLayer@Image>
    sint_hint: .5, .5
    source: "images/kivymd.png"
    pos_hint: {"center_x": .5, "center_y": .6}

<MyBackdropFrontLayer@ItemBackdropFrontLayer>
    backdrop: None
    text: "Lower the front layer"
    secondary_text: " by 50 %"
    icon: "transfer-down"
    on_press: root.backdrop.open(-Window.height / 2)
    pos_hint: {"top": 1}
    _no_ripple_effect: True
'''
)

Builder.load_string(
'''
<ExampleBackdrop>

    MDBackdrop:
        id: backdrop
        title: "Example Backdrop"
        left_action_items: [['menu', lambda x: self.open()]] # self: MDBackdrop object
        header_text: "Menu"

        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: backlayer

        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                backdrop: backdrop
                
''')

class ExampleBackdrop(Screen):
    pass

class TestBackdrop(MDApp):

    def build(self):
        return ExampleBackdrop()

TestBackdrop().run()