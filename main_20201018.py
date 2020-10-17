from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen
Window.size = (144*3, 256*3)

KV = '''
<Main@Screen>
    name: 'main'

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: 'MDLabel'

        MDLabel:
            id: label
            canvas.before:
                Color:
                    rgba: 0, 0, 1, .7
                Rectangle:
                    pos: self.pos
                    size: self.size
            text: "MDLabel"
            color: 0, 1, 0, .5
            halign: 'center'
            size_hint_y: 0.6

        MDSlider:
            size_hint_y: 0.4
            min: 0
            max: 100
            value: 40
            on_touch_move: root.slider_move(*args)
    
Main:
'''

class Main(Screen):
    def slider_move(self, instance_slider, mouse_motion):
        self.ids.label.text = str(instance_slider.value/100)
        instance_slider.size_hint_y = instance_slider.value/100
        self.ids.label.size_hint_y = 1-instance_slider.value/100

class MyApp(MDApp):
    def build(self):
        main = Builder.load_string(KV)
        return main
        

MyApp().run()