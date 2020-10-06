from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = (300, 500)

KV = '''
#:import MDListBottomSheet kivymd.uix.bottomsheet.MDListBottomSheet
#:import MDGridBottomSheet kivymd.uix.bottomsheet.MDGridBottomSheet
#:import MDDataTable kivymd.uix.datatables.MDDataTable
#:import dp kivy.metrics.dp
#:import toast kivymd.toast.toast

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
            md_bg_color: app.theme_cls.primary_dark

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

        MDFloatLayout:
            md_bg_color: app.theme_cls.primary_light

            MDRaisedButton:
                text: "Open list bottom sheet"
                on_release:
                    bottom_sheet_menu = MDGridBottomSheet()
                    bottom_sheet_menu.add_item("Standard Item", lambda x: toast("youtube"), icon_src="youtube")
                    bottom_sheet_menu.open()
                pos_hint: {"center_x": .5, "center_y": .8}

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
                pos_hint: {"center_x": .5, "center_y": .3}

        MDTextField:
            hint_text: "This is hint text"

        MDFloatingActionButton:
            icon: "plus"
'''

class Test(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)

Test().run()