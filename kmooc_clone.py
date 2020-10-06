from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.icon_definitions import md_icons
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.card import MDCard
from kivymd import images_path
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

Screen:
    name: "MainScreen"

    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "My Lecture Room"
            pos_hint: {"top": 1}
            left_action_items: [["menu", lambda x: x]]
            right_action_items: [["cog", lambda x: x]]
            elevation: 10

        MDTabs:
            Tab:
                text: "My Lecture Room"

                ScrollView:
                    MDBoxLayout:
                        id: lectures
                        padding: 10
                        spacing: 10
                        orientation: "vertical"
                        adaptive_height: True                     

            Tab:
                text: "K-MOOC Lecture"

<Card>
    elevation: 10
    size_hint: 1., None  
    size: 100, 200
    radius: (10, )
    on_release: print(root.title)

    BoxLayout:
        orientation: "vertical"

        FitImage:
            id: bg_image
            source: f"images/{root.img}" 
            size_hint_y: .6
            pos_hint: {"top": 1}
            radius: [10, 10, 0, 0, ]

        TwoLineListItem:
            text: root.title
            secondary_text: root.end_date
'''

class Card(MDCard):
    title = StringProperty()
    end_date = StringProperty()
    img = StringProperty()

class Tab(FloatLayout, MDTabsBase):
    pass

class Test(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)   

    def on_start(self):
        card_list = []
        card = Card(
            title="What's Literature?",
            end_date="Closed(Closing Date: 1st Feb)",
            img="book.jfif"
        )
        card_list.append(card)
        card = Card(
            title="Data Mining for Business Administration",
            end_date="Closed(Closing Date: 15th Feb)",
            img="data_mining.png"
        )
        card_list.append(card)
        card = Card(
            title="What's Literature?",
            end_date="Closed(Closing Date: 1st Feb)",
            img="book.jfif"
        )
        card_list.append(card)
        card = Card(
            title="Data Mining for Business Administration",
            end_date="Closed(Closing Date: 15th Feb)",
            img="data_mining.png"
        )
        card_list.append(card)
        card = Card(
            title="What's Literature?",
            end_date="Closed(Closing Date: 1st Feb)",
            img="book.jfif"
        )
        card_list.append(card)
        card = Card(
            title="Data Mining for Business Administration",
            end_date="Closed(Closing Date: 15th Feb)",
            img="data_mining.png"
        )
        card_list.append(card)
        
        for card in card_list:
            self.root.ids.lectures.add_widget(card)

Test().run()