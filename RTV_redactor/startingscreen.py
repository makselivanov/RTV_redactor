from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class StartingScreen(Screen):

    def __init__(self, **kwargs):
        super(StartingScreen, self).__init__(**kwargs)
        '''
        with self.canvas:
            Color(1, 0, 0, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)
        '''
        gl_menu = GridLayout(cols=1, size_hint=(.4, .4), pos_hint={'x': .29, 'y': .35})
        label = Label(text='\n\n\n         Welcome to RTV_redactor!\nChoose the action with project to start')
        gl_menu.add_widget(label)
        bl_buttons = BoxLayout(padding=1, size_hint=(.4, .4))
        self.btn_create = Button(text='Create')
        self.btn_open = Button(text='Open')
        bl_buttons.add_widget(self.btn_open)
        bl_buttons.add_widget(self.btn_create)
        gl_menu.add_widget(bl_buttons)

        fl = FloatLayout()
        fl.add_widget(gl_menu)
        self.add_widget(fl)

    def bindings(self, create, load):
        self.btn_create.bind(on_release=create)
        self.btn_open.bind(on_release=load)
