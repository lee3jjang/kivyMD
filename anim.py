from kivy.lang import Builder
from kivy.animation import Animation

from kivymd.app import MDApp

KV = '''
Screen:
    MDIconButton:
        icon: "android"
        pos_hint: {"center_x": .5, "center_y": .5}

    Button:
        on_release: app.animate(self)
        text: 'plop'
        size_hint: None, None
        pos_hint: {"center_x": .5, "center_y": .3}
'''

class TestApp(MDApp):

    def animate(self, inst):
        anim = Animation(pos_hint={'center_x': 0.7}, d=.2)
        anim = Animation(pos_hint={'center_x': 0.1}, d=.2)
        anim &= Animation(size=(500, 500), d=.2)
        anim += Animation(size=(100, 50), d=.1)

        anim.start(inst)

    def build(self):
        return Builder.load_string(KV)

TestApp().run()
