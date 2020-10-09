# from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
import json

# class MyApp(MDApp):
#     def build(self):
#         return Builder.load_file('libs/kv/start_screen.kv')

# MyApp().run()

with open('screens_data.json') as json_file:
    data_screens = json.load(json_file)
for name_item_example in data_screens:
    data = {
        'text': name_item_example,
        'icon': data_screens[name_item_example]['icon'],
    }

    print(data['icon'])
    