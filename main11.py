from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast

KV = '''
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "MDFileManager"
        left_action_items: [["menu", lambda x: None]]
        elevation: 10

    FloatLayout:
        MDRoundFlatIconButton:
            text: "Open manager"
            icon: "folder"
            pos_hint: {'center_x': .5, 'center_y': .1}
            on_release: app.file_manager_open()
'''

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Hello MyApp"
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        )

    def build(self):
        return Builder.load_string(KV)

    def file_manager_open(self):
        print("Hello File Manager!")
        self.file_manager.show('/')
        self.manager_open = True

    def exit_manager(self, *args):
        print("Bye File Manager!")
        self.manager_open = False
        self.file_manager.close()
    
    def select_path(self, path):
        self.exit_manager()
        toast(path)

MyApp().run()