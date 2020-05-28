from kivy.uix.screenmanager import ScreenManager

from RTV_redactor.mainscreen import MainScreen
from RTV_redactor.startingscreen import StartingScreen


class ManagerScreen(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start = StartingScreen(name='start')
        self.start.bindings(self.create, self.load)
        self.window = MainScreen(name='main')
        self.add_widget(self.start)
        self.add_widget(self.window)

    def create(self, instance):
        self.switch_to(self.window)
        self.window.win.saving_menu.open()

    def load(self, instance):
        self.switch_to(self.window)
        self.window.win.loading_menu.open()
