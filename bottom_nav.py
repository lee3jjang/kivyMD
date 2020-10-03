# from kivy.lang import Builder
# from kivy.factory import Factory
# from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
# from kivymd.uix.button import MDFlatButton
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider

from kivymd.uix.navigationdrawer import NavigationLayout, MDNavigationDrawer
# from kivy.uix.widget import Widget

Window.size = 144*3, 256*3

class ContentNavigationDrawer(MDBoxLayout):
    pass

class Example(MDApp):
    title = 'Hello My App!'

    def __init__(self):
        super().__init__()
        self.theme_cls.primary_palette = 'Teal'

    def build(self):

        ############## 0. 레이아웃  ##############
        layout = MDBoxLayout(orientation='vertical')


        ############## 1. 툴바      ##############
        toolbar = MDToolbar(title="Navigation Drawer")
        toolbar.left_action_items = [['menu', lambda x: x]]
        layout.add_widget(toolbar)
        

        ############## 1-2. 슬라이더 ###############
        slider = MDSlider(min=0, max=50, value=40)
        layout.add_widget(slider)
        slider.bind(on_touch_down=lambda inst, pos: print(inst))


        ############## 2. 하단 네비  ##############
        bottomnav = MDBottomNavigation()

        # Python
        bottomnav_item1 = MDBottomNavigationItem(
            name='Screen 1',
            text='Python',
            icon='language-python'
        )
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
        layout.add_widget(bottomnav)

        return layout

app = Example()
app.run()