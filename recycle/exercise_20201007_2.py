from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd.uix.boxlayout import MDBoxLayout
Window.size = (300, 500)

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

    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Example"
            pos_hint: {"top": 1}
            left_action_items: [["menu", lambda x: print(x)]]
            elevation: 10

        MDTabs:
            id: tabs

            MDTabsBase:
                text: "Tab 1"
            MDTabsBase:
                text: "Tab 2"
            MDTabsBase:
                text: "Tab 3"
            MDTabsBase:
                text: "Tab 4"
            MDTabsBase:
                text: "Tab 5"

        MDGridLayout:
            cols: 2
            md_bg_color: app.theme_cls.primary_light

            MDRoundFlatButton:
                text: "Button"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release:
                    print(spin)

            MDRaisedButton:
                text: "Open list bottom sheet"
                on_release:
                    bottom_sheet_menu = MDGridBottomSheet()
                    bottom_sheet_menu.add_item("Standard Item", lambda x: toast("youtube"), icon_src="youtube")
                    bottom_sheet_menu.open()
                # pos_hint: {"center_x": .5, "center_y": .8}

            MDRaisedButton:
                text: "datatable open"
                on_release:
                    data_table = MDDataTable(size_hint=(0.9, 0.6), \
                        column_data=[ \
                            ("No.", dp(30)), \
                            ("Column 1", dp(30)), \
                            ("Column 2", dp(30)), \
                            ("Column 3", dp(30)), \
                            ("Column 4", dp(30)), \
                            ("Column 5", dp(30)), \
                        ], \
                        row_data=[ \
                            (f"{i + 1}", "2.23", "3.65", "44.1", "0.45", "62.5") for i in range(50) \
                        ], \
                    )
                    data_table.open()
                # pos_hint: {"center_x": .5, "center_y": .3}

            MDRectangleFlatIconButton:
                icon: "android"
                text: "anddddddddddd"
                on_release:
                    snackbar = Snackbar(text="This is snakar")
                    snackbar.open()
                    pbar.value = 70

        ScrollView:
            MDGridLayout:
                id: mybox
                cols: 1
                adaptive_height: True
            
        MDProgressBar:
            id: pbar
            value: 50

        MDTextField:
            hint_text: "This is hint text"

        MDFloatingActionButton:
            icon: "plus"

        MDSpinner:
            id: spin
            size_hint: None, None
            size: dp(48), dp(48)
            pos_hint: {'center_x': .5, 'center_y': .5}

<Content>
    adaptive_height: True
 
    TwoLineIconListItem:
        text: "010-3013-xxxx"
        secondary_text: "lee3jjang"

        IconLeftWidget:
            icon: 'google'
'''

class Content(MDBoxLayout):
    pass

class Test(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)

    def on_start(self):
        self.root.ids.mybox.add_widget(
            MDExpansionPanel(
                content=Content(),
                panel_cls=MDExpansionPanelThreeLine(
                    text="text",
                    secondary_text="Secondary text",
                    tertiary_text="Tertiary text",
                )
            )
        )

        self.root.ids.mybox.add_widget(
            MDExpansionPanel(
                content=Content(),
                panel_cls=MDExpansionPanelThreeLine(
                    text="text",
                    secondary_text="Secondary text",
                    tertiary_text="Tertiary text",
                )
            )
        )
    

Test().run()