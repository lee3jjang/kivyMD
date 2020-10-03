# from kivy.lang import Builder
# from kivy.factory import Factory
# from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

from kivymd.app import MDApp
# from kivymd.uix.button import MDFlatButton
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
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

        nav_layout = NavigationLayout()
        screen = Screen()
        screen2 = Screen()
        screen_manager = ScreenManager()
        layout = MDBoxLayout(orientation='vertical')
        toolbar = MDToolbar(title="Navigation Drawer")
        toolbar.left_action_items = [['menu', lambda x: x]]
        content_nav_drawer = ContentNavigationDrawer()
        nav_drawer = MDNavigationDrawer()
        nav_drawer.id = 'nav_drawer'
        nav_drawer.add_widget(content_nav_drawer)
        
        screen.add_widget(nav_layout)
        nav_layout.add_widget(screen_manager)
        nav_layout.add_widget(nav_drawer)
        screen_manager.add_widget(screen2)
        screen2.add_widget(layout)
        layout.add_widget(toolbar)


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

        ############## 3. 네비 드로워 ##############

        
        bottomnav.add_widget(bottomnav_item1)
        bottomnav_item1.add_widget(label1)
        bottomnav.add_widget(bottomnav_item2)
        bottomnav_item2.add_widget(label2)
        bottomnav.add_widget(bottomnav_item3)
        bottomnav_item3.add_widget(label3)

        
        layout.add_widget(bottomnav)



        return screen

app = Example()
app.run()