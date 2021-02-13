from kivymd.app import MDApp
from kivy.lang.builder import Builder

KV = '''
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "Bottom navigation"
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, 1, 1, 1
        

    MDBottomNavigation:
        panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Python'
            icon: 'language-python'

            MDBoxLayout:
                orientation: "horizontal"

                MDLabel:
                    text: 'Python'
                    halign: 'center'
                MDLabel:
                    text: 'C++'
                    halign: 'center'
                MDLabel:
                    canvas:
                        Color:
                            rgba: 0, 0, 1, 0.5
                        Ellipse:
                            pos: self.pos
                            size: self.size
                    text: 'JS'
                    halign: 'center'


        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'C++'
            icon: 'language-cpp'

            MDLabel:
                text: 'I programming of C++'
                halign: 'center'
        
        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'JS'
            icon: 'language-javascript'

            MDLabel:
                text: 'JS'
                halign: 'center'
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()