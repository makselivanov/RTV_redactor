from kivy.uix.screenmanager import Screen
from window import Window


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.win = Window(orientation='vertical')
        self.add_widget(self.win)
