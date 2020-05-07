from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

"""
    Here main buttons added to menu
    
"""

_colors = ['White', 'Red', 'Green', 'Blue', 'Black']
_widths = ['2', '5', '8', '50']


class Menu(BoxLayout):
    """
         Class Menu has main buttons for working with application

         Static method 'bindings' is destined for setting actions with canvas to buttons of menu

    """

    def __init__(self, canvas_, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self._dropdown_color = DropDown()
        self._dropdown_width = DropDown()
        self.canvas_ = canvas_

        self._dropdown_color.add_widget(Button(text='%s' % _colors[0], color=(0, 0, 0, 1), size_hint_y=None, height=44,
                                               background_normal='', background_color=(0, 0, 0, 1),
                                               on_release=self.change_color))
        self._dropdown_color.add_widget(Button(text='%s' % _colors[1], color=(1, 0, 0, 1), size_hint_y=None, height=44,
                                               background_normal='', background_color=(1, 0, 0, 1),
                                               on_release=self.change_color))
        self._dropdown_color.add_widget(Button(text='%s' % _colors[2], color=(0, 1, 0, 1), size_hint_y=None, height=44,
                                               background_normal='', background_color=(0, 1, 0, 1),
                                               on_release=self.change_color))
        self._dropdown_color.add_widget(Button(text='%s' % _colors[3], color=(0, 0, 1, 1), size_hint_y=None, height=44,
                                               background_normal='', background_color=(0, 0, 1, 1),
                                               on_release=self.change_color))

        self._dropdown_color.bind(on_select=lambda instance, x: setattr(self._btn_color, 'text', x))

        for i in _widths:
            self._dropdown_width.add_widget(Button(text=i, size_hint_y=None, height=44, on_release=self.change_width))

        self._dropdown_width.bind(on_select=lambda instance, x: setattr(self._btn_width, 'text', x))

        self._btn_save = Button(text='Save', font_size=24)
        self._btn_load = Button(text='Load', font_size=24)
        self._btn_edit = Button(text='Edit', font_size=24)
        self._btn_back = Button(text='Back', font_size=24)
        self._btn_color = Button(text='Color', font_size=24, on_release=self._dropdown_color.open)
        self._btn_width = Button(text='Width', font_size=24, on_release=self._dropdown_width.open)
        self._btn_clear = Button(text='Clear', font_size=24)

        self.add_widget(self._btn_save)
        self.add_widget(self._btn_load)
        self.add_widget(self._btn_edit)
        self.add_widget(self._btn_back)
        self.add_widget(self._btn_color)
        self.add_widget(self._btn_width)
        self.add_widget(self._btn_clear)

    def bindings(self, save=None, load=None, back=None, clear=None):
        self._btn_save.bind(on_release=save)
        self._btn_load.bind(on_release=load)
        self._btn_back.bind(on_release=back)
        self._btn_clear.bind(on_release=clear)

    def change_color(self, instance):
        self._dropdown_color.select(instance.text)
        self.canvas_.change_color(instance)

    def change_width(self, instance):
        self._dropdown_width.select(instance.text)
        self.canvas_.change_width(instance)

    def choose_eraser(self, instance):
        instance.text = 'Eraser'
        self.canvas_.pen_color = (1, 1, 1, 1)

    def empty(self, instance):
        pass
