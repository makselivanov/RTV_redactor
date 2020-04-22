from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

"""
    Here main buttons added to menu
    
    Buttons can not change state of pen yet
    
"""

_colors = ['White', 'Red', 'Green', 'Blue', 'Black']
_widths = ['Thin', 'Medium', 'Thick']

_dropdown_color = DropDown()
_dropdown_width = DropDown()

_dropdown_color.add_widget(Button(text='%s' % _colors[0], color=(1, 1, 1, 1), size_hint_y=None, height=44,
                                  on_release=lambda instance: _dropdown_color.select(instance.text)))
_dropdown_color.add_widget(Button(text='%s' % _colors[1], color=(1, 0, 0, 1), size_hint_y=None, height=44,
                                  on_release=lambda instance: _dropdown_color.select(instance.text)))
_dropdown_color.add_widget(Button(text='%s' % _colors[2], color=(0, 1, 0, 1), size_hint_y=None, height=44,
                                  on_release=lambda instance: _dropdown_color.select(instance.text)))
_dropdown_color.add_widget(Button(text='%s' % _colors[3], color=(0, 0, 1, 1), size_hint_y=None, height=44,
                                  on_release=lambda instance: _dropdown_color.select(instance.text)))

_dropdown_color.bind(on_select=lambda instance, x: setattr(_btn_color, 'text', x))

_dropdown_width.add_widget(Button(text='%s' % _widths[0], size_hint_y=None, height=44,
                                  on_release=lambda instance: _dropdown_width.select(instance.text)))
_dropdown_width.add_widget(Button(text='%s' % _widths[1], size_hint_y=None, height=44,
                                  on_release=lambda instance: _dropdown_width.select(instance.text)))
_dropdown_width.add_widget(Button(text='%s' % _widths[2], size_hint_y=None, height=44,
                                  on_release=lambda instance: _dropdown_width.select(instance.text)))

_dropdown_width.bind(on_select=lambda instance, x: setattr(_btn_width, 'text', x))


_btn_save = Button(text='Save', font_size=24)
_btn_edit = Button(text='Edit', font_size=24)
_btn_color = Button(text='Color', font_size=24, on_release=_dropdown_color.open)
_btn_width = Button(text='Width', font_size=24, on_release=_dropdown_width.open)
_btn_clear = Button(text='Clear', font_size=24)


class Menu(BoxLayout):
    """
         Class Menu has main buttons for working with application

         Static method 'bindings' is destined for setting actions to buttons of menu

    """

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.add_widget(_btn_save)
        self.add_widget(_btn_edit)
        self.add_widget(_btn_color)
        self.add_widget(_btn_width)
        self.add_widget(_btn_clear)

    @staticmethod
    def bindings(save, clear):
        _btn_save.bind(on_release=save)
        _btn_clear.bind(on_release=clear)
