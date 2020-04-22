from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line

from kivy.core.window import Window


class CanvasWidget(Widget):
    """
        Class CanvasWidget has canvas for drawing in application

        Methods clear_canvas and save_canvas are used for buttons
        from menu.py and savingwidgets.py respectively

    """

    def __init__(self, **kwargs):
        super(CanvasWidget, self).__init__(**kwargs)
        self.filename = 'image.png'

    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 1, 1)
            rad = 5
            Ellipse(size=(rad, rad), pos=(touch.x - rad / 2, touch.y - rad / 2))
            touch.ud['track'] = Line(pos=(touch.x, touch.y), width=rad / 2)

    def on_touch_move(self, touch):
        touch.ud['track'].points += (touch.x, touch.y)

    def clear_canvas(self, instance):
        self.canvas.clear()

    def save_canvas(self, instance):
        self.size = (Window.size[0], Window.size[1])
        self.export_to_png(self.filename)
