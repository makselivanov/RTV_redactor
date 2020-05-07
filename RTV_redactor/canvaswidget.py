import json

from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle

from kivy.core.window import Window


class CanvasWidget(Widget):
    """
        Class CanvasWidget has canvas for drawing in application

        Methods clear_canvas and save_canvas are used for buttons
        from menu.py and savingmenu.py respectively

    """

    def __init__(self, saving_menu, loading_menu, manager,  **kwargs):
        super(CanvasWidget, self).__init__(**kwargs)
        self.track = None
        self._project_name = ''
        self._saving_menu = saving_menu
        self._loading_menu = loading_menu
        self.manager = manager
        self._pen_color = (0, 0, 0, 1)
        self._pen_width = 5
        self.shreds = []
        with self.canvas:
            Color(1, .9, .9, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_touch_down(self, touch):
        with self.canvas:
            Color(rgba=self._pen_color)
            rad = self._pen_width
            Ellipse(size=(rad, rad), pos=(touch.x - rad / 2, touch.y - rad / 2))
            touch.ud['track'] = Line(pos=(touch.x, touch.y), width=rad / 2)
        return super(CanvasWidget, self).on_touch_down(touch)

    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, name):
        self._project_name = name

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
        return super(CanvasWidget, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        try:
            if 'track' in touch.ud:  # условие, чтобы избежать ошибок при нажатии на кнопку
                if touch.ud['track'].points:
                    node = {
                        "color": self._pen_color,
                        "width": self._pen_width,
                        "points": touch.ud['track'].points
                    }
                    self.shreds.append(node)
                    self.manager.update_logs(json.dumps(node))
                else:
                    node = {
                        "color": self._pen_color,
                        "width": self._pen_width,
                        "points": list((touch.x, touch.y))
                    }
                    self.shreds.append(node)
                    self.manager.update_logs(json.dumps(node))
            return super(CanvasWidget, self).on_touch_up(touch)
        except FileNotFoundError:
            self._saving_menu.open()
            self.clear_canvas(touch)
            return super(CanvasWidget, self).on_touch_up(touch)

    def clear_canvas(self, instance):
        instance.text = instance.text
        self.canvas.clear()
        self.shreds.clear()
        with self.canvas:
            Color(1, .9, .9, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def save_project(self, instance):
        instance.text = 'Save'
        self._project_name = self._saving_menu.text_input.text
        self.size = (Window.size[0], Window.size[1])
        self.manager.creation(self.project_name)
        self.export_to_png(self.manager.path_image)
        self._saving_menu.dismiss()

    def load_project(self, instance):
        instance.text = 'Load'
        with self.canvas:
            Color(1, .9, .9, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)
        self._project_name = self._loading_menu.text_input.text
        self._saving_menu.text_input.text = self._project_name
        self.manager.loading(self._project_name)
        self.import_project(self.manager.path_logs)
        self._loading_menu.dismiss()

    def delete_last_shred(self, instance):
        instance.text = 'Back'
        with self.canvas:
            Color(.9, .9, .9, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.manager.delete_last_node()
        self.clear_canvas(instance)
        self.import_project(self.manager.path_logs)

    def change_color(self, instance):
        self.pen_color = instance.background_color

    def change_width(self, instance):
        self.pen_width = int(instance.text)

    def import_project(self, logs):
        with open(logs, 'tr') as f:
            for line in f.readlines():
                if line != '\n':
                    string = line.rstrip('\n')
                    self.shreds.append(json.loads(string))
        with self.canvas:
            for shred in self.shreds:
                Color(rgba=shred["color"])
                width = int(shred["width"])
                for i in range(0, len(shred["points"]) - 3, 2):
                    with self.canvas:
                        line = Line(points=(shred["points"][i], shred["points"][i+1]), width=width / 2)
                        line.points += (shred["points"][i+2], shred["points"][i+3])
