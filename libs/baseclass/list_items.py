from kivy.properties import ListProperty, StringProperty
from kivymd.uix.list import OneLineAvatarListItem, OneLineIconListItem, TwoLineAvatarListItem



class KitchenSinkOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()

class KitchenSinkOneLineLeftIconItem(OneLineAvatarListItem):
    icon = StringProperty()

class KitchenSinkTwoLineLeftAvatarItem(TwoLineAvatarListItem):
    icon = StringProperty()
    secondary_font_style = 'Caption'

class KitchenSinkOneLineLeftAvatarItem(OneLineAvatarListItem):
    divider = None
    source = StringProperty()

class KitchenSinkOneLineLeftWidgetItem(OneLineAvatarListItem):
    color = ListProperty()