from kivy.lang import Builder
from kivymd.app import MDApp
from datetime import datetime
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivymd.utils.hot_reload_viewer import HotReloadViewer
from kivy.extras.highlight import KivyLexer

class Example(MDApp):
    path_to_kv_file = "regis.kv"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        
        boxlayout = BoxLayout()
        code = ''
        with open(self.path_to_kv_file, "r") as kv_file:
            code = kv_file.read()
        codeinput = CodeInput(
            text=code,
            lexer=KivyLexer(),
            style_name="native",
            size_hint_x=.6,
        )
        codeinput.bind(text=self.update_kv_file)
        hot_reload_viewer = HotReloadViewer(
            size_hint_x=.4,
            path=self.path_to_kv_file,
            errors=True,
            errors_text_color=(1, 1, 0, 1),
            errors_background_color=self.theme_cls.bg_dark,
        )
        boxlayout.add_widget(codeinput)
        boxlayout.add_widget(hot_reload_viewer)

        return boxlayout

    def update_kv_file(self, instnce, text):
        with open(self.path_to_kv_file, "w") as kv_file:
            kv_file.write(text)

Example().run()
