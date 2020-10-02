from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

class Example(MDApp):
    def build(self):
        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            use_pagination=True,
            check=True,
            column_data=[
                ("No.", dp(30)),
                ("Column 1", dp(30)),
                ("Column 2", dp(30)),
                ("Column 3", dp(30)),
                ("Column 4", dp(30)),
                ("Column 5", dp(30)),
            ],
            row_data=[
                (f'{i+1}', '4.1', '2.3', '82', '2.3', '0.82') for i in range(10)
            ]
        )
        self.data_tables.bind(on_row_press = self.on_row_press)
        self.data_tables.bind(on_check_press = self.on_check_press)

    def on_row_press(self, inst_table, inst_row):
        print(inst_table, inst_row)

    def on_check_press(self, inst_table, inst_row):
        print(inst_table, inst_row)

    def on_start(self):
        self.data_tables.open()


Example().run()