from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDFloatLayout:
    MDCheckbox:
        id: box1
        group: 'grp'
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .4, 'center_y': .5}

    MDCheckbox:
        id: box2
        group: 'grp'
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .6, 'center_y': .5}
    
    MDIconButton:
        icon: "language-python"
        size_hint: None, None
        size: "96dp", "96dp"
        pos_hint: {'center_x': .5, 'center_y': .3}
        on_release: app.test()


'''

class Test(MDApp):
    def test(self):
        print("test")

    def build(self):
        return Builder.load_string(KV)

Test().run()