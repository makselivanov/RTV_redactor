from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class SavingMenu(Popup):
    """
        Class SavingMenu is popup window, where user can enter file name for save.
        But now user can`t do this, he can save in image.png only

        Method bindings is destined for setting actions to buttons of saving menu

    """

    def __init__(self, **kwargs):
        super(SavingMenu, self).__init__(**kwargs)
        bl = BoxLayout(orientation='vertical')
        buttons = BoxLayout(size_hint=(1, .5))
        self.btn_save = Button(text='Save')
        self.btn_cancel = Button(text='Cancel', on_release=self.dismiss)
        buttons.add_widget(self.btn_save)
        buttons.add_widget(self.btn_cancel)
        self.text_input = TextInput(size_hint=(1, .2), multiline=False)
        bl.add_widget(self.text_input)
        bl.add_widget(buttons)
        self.add_widget(bl)

    def bindings(self, save):
        self.btn_save.bind(on_release=save)
