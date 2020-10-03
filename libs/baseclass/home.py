from kivy.animation import Animation
from kivy.uix.screenmanager import Screen

class Home(Screen):
    def opening_animation_backdrop_components(self, inst_backdrop, inst_backlayer):
        Animation(scale_x=1, scale_y=1, d=.2).start(inst_backlayer)
        anim = Animation(opacity=0, d=.2)
        anim.bind(on_complete=self.set_instance_backdrop_title)
        anim.start(inst_backdrop.ids.toolbar.ids.label_title)

    def set_instance_backdrop_title(self, inst_animation, inst_backdrop):
        inst_backdrop.text = ('Menu' if inst_backdrop.text == 'Kitchen Sink' else 'Kitchen Sink')
        Animation(opacity=1, d=2).start(inst_backdrop)