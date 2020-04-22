from kivy.uix.boxlayout import BoxLayout

from canvaswidget import CanvasWidget
from menu import Menu
from savingmenu import SavingMenu


class Window(BoxLayout):
    """
        In this class all components are merged in main window.

        Here materializes bindings actions to buttons save, clear

    """

    def __init__(self, **kwargs):
        super(Window, self).__init__(**kwargs)
        self.working_space = CanvasWidget()
        self.menu = Menu(size_hint=(1, .2))
        self.saving_menu = SavingMenu(title='Save to', size_hint=(.4, .3))
        self.saving_menu.bindings(self.working_space.save_canvas)
        self.menu.bindings(save=self.saving_menu.open, clear=self.working_space.clear_canvas)
        self.add_widget(self.working_space)
        self.add_widget(self.menu)
