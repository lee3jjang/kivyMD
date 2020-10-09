
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        titie: "MDFileManager"
        left_action_items: [['menu', lambda x: print("Menu is Clicked")]]
        elevation: 10

    FloatLayout:
        MDRoundFlatIconButton:
            text: "Open manager"
            icon: "folder"
            pos_hint: {'center_x': .5, 'center_y': .6}
            on_release: app.file_manager_open()
'''

class MyApp(MDApp):
    def __init__(self):
        super().__init__()
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager = self.exit_manager,
            select_path = self.select_path,
            preview=False,
        )

    def file_manager_open(self):
        self.file_manager.show('.')
        self.manager_open = True

    def select_path(self, path):
        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        print(args)
        self.manager_open = False
        self.file_manager.close()

    def build(self):
        return Builder.load_string(KV)

MyApp().run()