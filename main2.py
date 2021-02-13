from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (960, 1009)
Window.position = 'custom'
Window.left, Window.top = (960, -1049)


KV = """
Screen:
"""

class MyApp(App):
    ticks = 0

    def build(self):
        self.event = Clock.schedule_interval(self.update, 1.)
        return Builder.load_string(KV)

    def update(self, dt):
        self.ticks += 1
        print(self.ticks)
        if self.ticks == 5:
            print("Unscheduled")
            Clock.unschedule(self.event)

MyApp().run()
