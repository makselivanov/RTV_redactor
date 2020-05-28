from kivy.uix.boxlayout import BoxLayout

from RTV_redactor.canvaswidget import CanvasWidget
from RTV_redactor.menu import Menu
from RTV_redactor.savingmenu import SavingMenu
from RTV_redactor.loadingmenu import LoadingMenu
from RTV_redactor.project_manager import ProjectManager


class Window(BoxLayout):
    """
        In this class all components are merged in main window.

        Here materializes bindings actions to buttons

    """

    def __init__(self, **kwargs):
        super(Window, self).__init__(**kwargs)
        self.saving_menu = SavingMenu(title='Project name', size_hint=(.4, .3))
        self.loading_menu = LoadingMenu(title='Load project', size_hint=(.4, .3))
        self.project_manager = ProjectManager()
        self.working_space = CanvasWidget(self.saving_menu, self.loading_menu, self.project_manager)
        self.menu = Menu(self.working_space, size_hint=(1, .12))
        self.saving_menu.bindings(save=self.working_space.save_project)
        self.loading_menu.bindings(load=self.working_space.load_project)
        self.menu.bindings(save=self.saving_menu.open,
                           load=self.loading_menu.open,
                           back=self.working_space.delete_last_shred,
                           clear=self.working_space.clear_canvas)
        self.add_widget(self.working_space)
        self.add_widget(self.menu)
