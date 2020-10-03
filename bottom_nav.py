# from kivy.lang import Builder
# from kivy.factory import Factory
# from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivymd.app import MDApp
# from kivymd.uix.button import MDFlatButton
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

Window.size = 144*3, 256*3

class Example(MDApp):
    title = 'Hello My App!'

    def __init__(self):
        super().__init__()
        self.theme_cls.primary_palette = 'Teal'

    def build(self):
        layout = MDBoxLayout(
            orientation='vertical',
            # size_hint=(None, None),
            # pos_hint={'center_x': .5, 'center_y': .5},
        )

        # 툴바
        toolbar = MDToolbar(
            title="Bottom navigation",
            # left_action_items=[['menu', lambda x: x]],
        )

        bottomnav = MDBottomNavigation()

        # Python
        bottomnav_item1 = MDBottomNavigationItem(
            name='Screen 1',
            text='Python',
            icon='language-python'
        )

        # 이게 중간 화면에 나옴
        label1 = MDLabel(
            text='Python',
            halign='center'
        )

        # C++
        bottomnav_item2 = MDBottomNavigationItem(
            name='Screen 2',
            text='C++',
            icon='language-cpp'
        )
        label2 = MDLabel(
            text='I programming of C++',
            halign='center'
        )

        # JS
        bottomnav_item3 = MDBottomNavigationItem(
            name='Screen 3',
            text='JS',
            icon='language-javascript'
        )
        label3 = MDLabel(
            text='JS',
            halign='center'
        )
        
        bottomnav.add_widget(bottomnav_item1)
        bottomnav_item1.add_widget(label1)
        bottomnav.add_widget(bottomnav_item2)
        bottomnav_item2.add_widget(label2)
        bottomnav.add_widget(bottomnav_item3)
        bottomnav_item3.add_widget(label3)

        layout.add_widget(toolbar)
        layout.add_widget(bottomnav)



        return layout

app = Example()
app.run()