from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line

from kivy.core.window import Window


class CanvasWidget(Widget):
    """
        Class CanvasWidget has canvas for drawing in application

        Methods clear_canvas and save_canvas are used for buttons
        from menu.py and savingmenu.py respectively

    """

    def __init__(self, saving_menu, **kwargs):
        super(CanvasWidget, self).__init__(**kwargs)
        self._filename = ''
        self._saving_menu = saving_menu
        self._pen_color = ([1, 1, 1, 1])
        self._pen_width = 5

    def on_touch_down(self, touch):
        with self.canvas:
            Color(rgba=self._pen_color)
            rad = self._pen_width
            Ellipse(size=(rad, rad), pos=(touch.x - rad / 2, touch.y - rad / 2))
            touch.ud['track'] = Line(pos=(touch.x, touch.y), width=rad / 2)

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, name):
        self._filename = name

    @property
    def pen_color(self):
        return self._pen_color

    @pen_color.setter
    def pen_color(self, color):
        self._pen_color = color

    @property
    def pen_width(self):
        return self._pen_width

    @pen_width.setter
    def pen_width(self, width):
        self._pen_width = width

    def on_touch_move(self, touch):
        touch.ud['track'].points += (touch.x, touch.y)

    def clear_canvas(self, instance):
        instance.text = 'Clear'
        self.canvas.clear()

    def save_canvas(self, instance):
        instance.text = 'Save'
        self.filename = self._saving_menu.text_input.text
        self.size = (Window.size[0], Window.size[1])
        self.export_to_png(self.filename)
        self._saving_menu.dismiss()

    def change_color(self, instance):
        self.pen_color = instance.background_color

    def change_width(self, instance):
        self.pen_width = int(instance.text)
