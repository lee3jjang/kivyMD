from todo_crud import *
from datetime import date
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.factory import Factory
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem, TwoLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
Window.size = (144*3, 256*3)

KV = '''
<ListItemWithCheckbox>
    todo_id: root.todo_id
    
    IconLeftWidget:
        icon: root.icon

    RightCheckbox:
        on_active: self.on_checkbox_active(*args)

BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        id: toolbar        
        title: '투두'
        left_action_items: [['menu', lambda x: app.menu_callback(x)]]

    MDBottomNavigation:
        id: panel

        MDBottomNavigationItem:
            name: "all"
            text: "all"
            icon: "alpha-a-circle-outline"

            ScrollView:
                MDList:
                    id: todo_list_all

        MDBottomNavigationItem:
            name: "complete"
            text: "complete"
            icon: "alpha-c-circle-outline"

            ScrollView:
                MDList:
                    id: todo_list_complete

        MDBottomNavigationItem:
            name: "incomplete"
            text: "incomplete"
            icon: "alpha-i-circle-outline"

            ScrollView:
                MDList:
                    id: todo_list_incomplete

'''

class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    todo_id = NumericProperty()
    icon = StringProperty("android")

class RightCheckbox(IRightBodyTouch, MDCheckbox):
    def on_checkbox_active(self, instance_checkbox, is_checked):
        print(is_checked)


class TodoApp(MDApp):
    def build(self):
        root = Builder.load_string(KV)
        logo = root.ids.toolbar.ids.label_title
        logo.font_name = 'assets/fonts/NanumGothic.ttf'
        return root

    def on_start(self):
        rows = get_todo_all()
        for row in rows:
            todo = ListItemWithCheckbox(todo_id=row[0], text=row[1], secondary_text=row[2])
            todo.ids._lbl_secondary.font_name = 'assets/fonts/NanumGothic.ttf'
            todo.ids._lbl_primary.font_name = 'assets/fonts/NanumGothic.ttf'
            self.root.ids.todo_list_all.add_widget(todo)

        rows = get_todo_complete()
        for row in rows:
            todo = ListItemWithCheckbox(todo_id=row[0], text=row[1], secondary_text=row[2])
            todo.ids._lbl_secondary.font_name = 'assets/fonts/NanumGothic.ttf'
            todo.ids._lbl_primary.font_name = 'assets/fonts/NanumGothic.ttf'
            self.root.ids.todo_list_complete.add_widget(todo)

        rows = get_todo_not_complete()
        for row in rows:
            todo = ListItemWithCheckbox(todo_id=row[0], text=row[1], secondary_text=row[2])
            todo.ids._lbl_secondary.font_name = 'assets/fonts/NanumGothic.ttf'
            todo.ids._lbl_primary.font_name = 'assets/fonts/NanumGothic.ttf'
            self.root.ids.todo_list_incomplete.add_widget(todo)

    def menu_callback(self, instance_button):
        print(instance_button)

TodoApp().run()