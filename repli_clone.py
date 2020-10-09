from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.icon_definitions import md_icons
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.image import Image
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.card import MDCard
from kivymd import images_path
from kivymd.uix.list import ThreeLineAvatarListItem
from kivy.properties import StringProperty
Window.size = (144*3, 256*3)


KV = '''
#:import MDListBottomSheet kivymd.uix.bottomsheet.MDListBottomSheet
#:import MDGridBottomSheet kivymd.uix.bottomsheet.MDGridBottomSheet
#:import MDExpansionPanel kivymd.uix.expansionpanel.MDExpansionPanel
#:import MDDataTable kivymd.uix.datatables.MDDataTable
#:import Snackbar kivymd.uix.snackbar.Snackbar
#:import toast kivymd.toast.toast
#:import dp kivy.metrics.dp
#:import Window kivy.core.window.Window

Screen:
    name: "MainScreen"

    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "REPLI"
            halign: "center"
            pos_hint: {"top": 1}
            elevation: 0

        ScrollView:
            size_hint_y: None
            size_hint_x: None
            y: self.parent.y
            x: self.parent.x
            width: self.parent.width
            height: self.parent.height-100

            MDList:
                Button:
                    size_hint_y: None
                    size_hint_x: None
                    y: self.parent.y
                    x: self.parent.x
                    width: self.parent.width
                    height: self.parent.height/3.25
                    on_release: print("Button")
                    Image:
                        source: 'images/data_mining.png'
                        size_hint_y: None
                        size_hint_x: None
                        y: self.parent.y
                        x: self.parent.x
                        width: self.parent.width
                        height: self.parent.height
                        allow_stretch: True                


                ThreeLineAvatarListItem:
                    text: "2020.10.08 VOTING"
                    secondary_text: "Three Laws about Economy"
                    tertiary_text: "What's your choice?"
                    on_release: print("List")
                    ImageLeftWidget:
                        source: "images/img1.jpg"

                ThreeLineAvatarListItem:
                    text: "2020.10.08 VOTING"
                    secondary_text: "Three Laws about Economy"
                    tertiary_text: "What's your choice ?"
                    ImageLeftWidget:
                        source: "images/img1.jpg"

                ThreeLineAvatarListItem:
                    text: "2020.10.08 VOTING"
                    secondary_text: "Three Laws about Economy"
                    tertiary_text: "What's your choice?"
                    ImageLeftWidget:
                        source: "images/img1.jpg"

                ThreeLineAvatarListItem:
                    text: "2020.10.08 VOTING"
                    secondary_text: "Three Laws about Economy"
                    tertiary_text: "What's your choice?"
                    ImageLeftWidget:
                        source: "images/img1.jpg"

                ThreeLineAvatarListItem:
                    text: "2020.10.08 VOTING"
                    secondary_text: "Three Laws about Economy"
                    tertiary_text: "What's your choice?"
                    ImageLeftWidget:
                        source: "images/img1.jpg"

                ThreeLineAvatarListItem:
                    text: "2020.10.08 VOTING"
                    secondary_text: "Three Laws about Economy"
                    tertiary_text: "What's your choice?"
                    ImageLeftWidget:
                        source: "images/img1.jpg"

        MDBottomNavigation:
            
            MDBottomNavigationItem:
                # name: 'topic'
                text: 'TOPIC'
                icon: 'home'

            MDBottomNavigationItem:
                # name: 'history'
                text: 'HISTORY'
                icon: 'text-box-multiple'

            MDBottomNavigationItem:
                # name: 'search'
                text: 'SEARCH'
                icon: 'magnify'

            MDBottomNavigationItem:
                # name: 'alarm'
                text: 'ALARM'
                icon: 'bell'

            MDBottomNavigationItem:
                # name: 'acoount'
                text: 'ACCOUNT'
                icon: 'account'
'''

class Test(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)   

    def on_start(self):
        pass

Test().run()