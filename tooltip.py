from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
<TooltipMDIconButton@MDIconButton+MDTooltip>

Screen:
    TooltipMDIconButton:
        icon: "language-python"
        tooltip_text: "Hello Tooltip!"
        pos_hint: {'center_x': .5, 'center_y': .5}
'''

class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)



Test().run()