from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.factory import Factory
import json
Window.size = (144*3, 256*3)

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Teal"
        self.data_screens = {}

    def build(self):
        return Builder.load_file('libs/kv/start_screen.kv')

    def on_start(self):
        with open('screens_data.json') as read_file:
            self.data_screens = json.load(read_file)

        name_screen = list(self.data_screens.keys())[2]
        self.set_example_screen(name_screen)
        
    def set_example_screen(self, name_screen):
        # ScreenManager 객체 획득
        manager = self.root.ids.screen_manager
        # name: name_screen에 관한 configuration data 획득
        data_screen = self.data_screens[name_screen]
        # name: name_screen인 Screen 존재여부 검사
        if not manager.has_screen(name_screen):
            if 'Import' in data_screen:
                pass
                exec(data_screen['Import'])
            # .kv 파일 로드
            Builder.load_file(f'libs/kv/{data_screen["kv_string"]}.kv')
            # Screen 객체(위젯) 획득
            screen_object = eval(data_screen["Factory"])
            # ScreenManager 객체에 Screen 위젯 추가
            manager.add_widget(screen_object)
        # 현재 화면을 Screen 위젯으로 변경
        manager.current = data_screen["name_screen"]

if __name__ == '__main__':
    MyApp().run()
    # exec("print('hello')")
    # x = eval('4+2')
    # print(x)
    # f = lambda x=7: x+8
    # print(f(23))

    
