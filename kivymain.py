from todo_crud import *
from datetime import date
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.factory import Factory
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem, TwoLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
Window.size = (144*3, 256*3)

KV = '''
<AddContent>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"

    MDTextField:
        id: category
        hint_text: "Category"

    MDTextField:
        id: contents
        hint_text: "Contents"

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

        MDBottomNavigationItem:
            name: "incomplete"
            text: "incomplete"
            icon: "alpha-i-circle-outline"

            ScrollView:
                MDList:
                    id: todo_list_incomplete

        MDBottomNavigationItem:
            name: "complete"
            text: "complete"
            icon: "alpha-c-circle-outline"

            ScrollView:
                MDList:
                    id: todo_list_complete

        MDBottomNavigationItem:
            name: "all"
            text: "all"
            icon: "alpha-a-circle-outline"

            ScrollView:
                MDList:
                    id: todo_list_all

        

'''
class ListItemWithCheckbox(TwoLineAvatarIconListItem, TouchBehavior):
    todo_id = NumericProperty()
    icon = StringProperty("android")
    delete_dialog = None
    def on_long_touch(self, *args):
        def deleteButton(instance_button):
            id = self.todo_id
            delete_todo(id)
            app.renewal()
            self.delete_dialog.dismiss()

        if not self.delete_dialog:
            self.delete_dialog = MDDialog(
                text="Delete Todo?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release=lambda x: self.delete_dialog.dismiss()
                    ),
                    MDFlatButton(
                        text="DELETE", text_color=self.theme_cls.primary_color, on_release=deleteButton
                    ),
                ],
            )
        self.delete_dialog.open()
        

class RightCheckbox(IRightBodyTouch, MDCheckbox):
    def on_checkbox_active(self, instance_checkbox, is_checked):
        pass

class AddContent(BoxLayout):
    pass

class TodoApp(MDApp):
    menu = None
    add_dialog = None

    def build(self):
        global app
        app = self
        root = Builder.load_string(KV)
        logo = root.ids.toolbar.ids.label_title
        logo.font_name = 'assets/fonts/NanumGothic.ttf'
        return root

    def on_start(self):
        self.renewal()

    def renewal(self):
        rows = get_todo_not_complete()
        self.root.ids.todo_list_incomplete.clear_widgets()
        for row in rows:
            todo = ListItemWithCheckbox(todo_id=row[0], text=row[1], secondary_text=row[2])
            todo.ids._lbl_secondary.font_name = 'assets/fonts/NanumGothic.ttf'
            todo.ids._lbl_primary.font_name = 'assets/fonts/NanumGothic.ttf'
            self.root.ids.todo_list_incomplete.add_widget(todo)

        rows = get_todo_complete()
        self.root.ids.todo_list_complete.clear_widgets()
        for row in rows:
            todo = ListItemWithCheckbox(todo_id=row[0], text=row[1], secondary_text=row[2])
            todo.ids._lbl_secondary.font_name = 'assets/fonts/NanumGothic.ttf'
            todo.ids._lbl_primary.font_name = 'assets/fonts/NanumGothic.ttf'
            self.root.ids.todo_list_complete.add_widget(todo)

        rows = get_todo_all()
        self.root.ids.todo_list_all.clear_widgets()
        for row in rows:
            todo = ListItemWithCheckbox(todo_id=row[0], text=row[1], secondary_text=row[2])
            todo.ids._lbl_secondary.font_name = 'assets/fonts/NanumGothic.ttf'
            todo.ids._lbl_primary.font_name = 'assets/fonts/NanumGothic.ttf'
            self.root.ids.todo_list_all.add_widget(todo)

        

    def menu_callback(self, instance_button):
        # menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
        if self.menu == None:
            self.menu = MDDropdownMenu(
                caller = instance_button,
                items = [{'icon': 'plus', 'text': 'ADD'}],
                position = 'auto',
                width_mult = 4,
            )
        self.menu.bind(on_release=self.menu_action)
        self.menu.open()

    def menu_action(self, instance_menu, instance_menu_item):
        if instance_menu_item.text == 'ADD':
            if not self.add_dialog:
                def okButton(instance_button):
                    contents = self.add_dialog.content_cls.ids.contents.text
                    category = self.add_dialog.content_cls.ids.category.text
                    insert_todo(contents, category)
                    self.renewal()
                    self.add_dialog.dismiss()

                self.add_dialog = MDDialog(
                    title='Add Todo',
                    type='custom',
                    content_cls=AddContent(),
                    buttons=[
                        MDFlatButton(
                            text="CANCEL", text_color=self.theme_cls.primary_color, on_release=lambda x: self.add_dialog.dismiss()
                        ),
                        MDFlatButton(
                            text="OK", text_color=self.theme_cls.primary_color, on_release=okButton
                        ),
                    ],
                )
            self.add_dialog.open()
        self.menu.dismiss()
        
TodoApp().run()