from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class LoadingMenu(Popup):

    def __init__(self, **kwargs):
        super(LoadingMenu, self).__init__(**kwargs)
        bl = BoxLayout(orientation='vertical')
        buttons = BoxLayout(size_hint=(1, .5))
        self.btn_load = Button(text='Load')
        self.btn_cancel = Button(text='Cancel', on_release=self.dismiss)
        buttons.add_widget(self.btn_load)
        buttons.add_widget(self.btn_cancel)
        self.text_input = TextInput(size_hint=(1, .2), multiline=False)
        bl.add_widget(self.text_input)
        bl.add_widget(buttons)
        self.add_widget(bl)

    def bindings(self, load):
        self.btn_load.bind(on_release=load)
