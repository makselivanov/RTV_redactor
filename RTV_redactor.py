from kivy.app import App

from view import Window


class MainApp(App):
    """
        Launching of application

        Visit https://github.com/makselivanov/RTV_redactor for more information
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.window = Window(orientation='vertical')

    def build(self):
        return self.window


if __name__ == '__main__':
    MainApp().run()
