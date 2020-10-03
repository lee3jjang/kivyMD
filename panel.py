from kivy.lang import Builder

from kivymd import images_path
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine

KV = '''
<Content>
    adaptive_height: True

    # TwoLine : 텍스트가 두줄이다
    # Icon : 아이콘이 있다
    # ListItem : 리스트다
    TwoLineIconListItem:
        text: "(050)-123-45-67"
        secondary_text: "Mobile"

        IconLeftWidget:
            icon: 'android'

ScrollView:
    MDGridLayout:
        id: box
        cols: 1
        adaptive_height: True

'''

class Content(MDBoxLayout):
    pass

class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):

        for _ in range(10):
            self.root.ids.box.add_widget(
                # 확장패널인데
                # 아이콘은 kivymd
                # 컨텐츠는 위에 정의한거
                # 패널은 3라인
                MDExpansionPanel(
                    icon = f'images/kivymd.png',
                    content = Content(),
                    panel_cls = MDExpansionPanelThreeLine(
                        text = "Text",
                        secondary_text="Secondary text",
                        tertiary_text="Tertiary text",
                    )
                )
            )

Test().run()