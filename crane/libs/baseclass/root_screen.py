import os

from kivy.clock import Clock
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image

from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout

class CraneRootScreen(ThemableBehavior, MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._late_init)

    def _late_init(self, i):
        self.image = Image(
            source=f"{os.environ['CRANE_ROOT']}/assets/images/logo_light.png",
            size_hint=(None, None),
            size=("40dp","40dp"),
        )
        self.ids.tab.tab_bar.add_widget(self.image, index=1)

class CraneListItem(ThemableBehavior, MDBoxLayout):
    text = StringProperty()
    secondary_text = StringProperty()
    image = StringProperty()