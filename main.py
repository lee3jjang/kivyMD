from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.factory import Factory
import json
from libs.baseclass.list_items import KitchenSinkOneLineLeftIconItem
Window.size = (144*3, 256*3)

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Teal"
        self.data_screens = {}

    def build(self):
        Builder.load_file('libs/kv/list_items.kv')
        return Builder.load_file('libs/kv/start_screen.kv')

    def on_start(self):
        with open('screens_data.json') as read_file:
            self.data_screens = json.load(read_file)

        # name_screen = list(self.data_screens.keys())[0]
        # self.set_example_screen(name_screen)

        for name_item_example in self.data_screens:
            self.root.ids.backdrop_front_layer.data.append(
                {
                    "viewclass": "KitchenSinkOneLineLeftIconItem",
                    "icon": self.data_screens[name_item_example]["icon"],
                    "text": name_item_example,
                    "on_release": lambda x=name_item_example: self.set_example_screen(x)
                }
            )
        
    def set_example_screen(self, name_screen):
        # ScreenManager 객체 획득
        manager = self.root.ids.screen_manager
        # name: name_screen에 관한 configuration data 획득
        data_screen = self.data_screens[name_screen]
        # name: name_screen인 Screen 존재여부 검사
        if not manager.has_screen(data_screen['name_screen']):
            # bassclass에 정의된 클래스 Import
            if 'Import' in data_screen:
                exec(data_screen['Import'])
            # .kv 파일 로드
            Builder.load_file(f'libs/kv/{data_screen["kv_string"]}.kv')
            # Screen 객체(위젯) 획득
            screen_object = eval(data_screen["Factory"])
            # ScreenManager 객체에 Screen 위젯 추가
            manager.add_widget(screen_object)
        # 현재 화면을 Screen 위젯으로 변경
        manager.current = data_screen["name_screen"]

    def back_to_home_screen(self):
        self.root.ids.screen_manager.current = "home"

    def switch_theme_style(self):
        self.theme_cls.theme_style = "Light" if self.theme_cls.theme_style == "Dark" else "Light"

if __name__ == '__main__':
    MyApp().run()

    
