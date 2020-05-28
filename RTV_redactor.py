from kivy.app import App

from RTV_redactor.screens import ManagerScreen


class MainApp(App):
    """
        Launching of application

        Visit https://github.com/makselivanov/RTV_redactor for more information

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ms = ManagerScreen()

    def build(self):
        return self.ms


if __name__ == '__main__':
    MainApp().run()
