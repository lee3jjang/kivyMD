
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: 'Bottom navigation'
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, 1, 1, .8

    MDBottomNavigation:
        panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Python'
            icon: 'language-python'

            MDLabel:
                text: 'I am Python'
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

class Test(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Gray'
        return Builder.load_string(KV)

Test().run()