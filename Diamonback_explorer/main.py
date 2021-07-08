from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 10
    V_LINES_SPACING = .2  # 10% in screen width
    vertical_lines = []

    H_NB_LINES = 15
    H_LINES_SPACING = .2  # 10% in screen width
    horizontal_lines = []

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print("Init W: " + str(self.width) + " H: " + str(self.height))
        self.init_vertical_lines()
        self.init_horizontal_lines()

    def on_parent(self, widget, parent):
        print("On Parent W: " + str(self.width) + " H: " + str(self.height))

    def on_size(self, *args):
        self.update_vertical_lines()
        self.update_horizontal_lines()
        # I don't need this function I declare it in the diamonback.kv
        pass
        # print("On Size W: " + str(self.width) + " H: " + str(self.height))
        # self.perspective_point_x = self.width/2
        # self.perspective_point_y = self.height * 0.75

    def on_perspective_point_x(self, widget, value):
        # print("PX: " + str(value))
        pass

    def on_perspective_point_y(self, widget, value):
        # print("PY: " + str(value))
        pass

    #
    # Initialisation and update of verticale lines
    #
    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            # self.line = Line(points=[100, 0, 100, 100])
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def update_vertical_lines(self):
        # self.line.points = [self.perspective_point_x, 0, self.perspective_point_x, 100]
        central_line_x = self.width / 2
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NB_LINES / 2) + 0.5
        for i in range(0, self.V_NB_LINES):
            lines_x = int(central_line_x + offset * spacing)
            x1, y1 = self.transform(lines_x, 0)
            x2, y2 = self.transform(lines_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]
            offset += 1

    #
    # Initialisation and update of horizontal lines
    #
    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(Line())

    def update_horizontal_lines(self):
        central_line_x = self.width / 2
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NB_LINES / 2) + 0.5

        min_x = central_line_x + offset * spacing
        max_y = central_line_x - offset * spacing
        spacing_y = self.H_LINES_SPACING * self.height
        for i in range(0, self.H_NB_LINES):
            lines_y = int(i * spacing_y)
            x1, y1 = self.transform(min_x, lines_y)
            x2, y2 = self.transform(max_y, lines_y)
            self.horizontal_lines[i].points = [x1, y1, x2, y2]

    # intermediate function to change the behaviour of the display without changing all the code
    def transform(self, x, y):
        # return self.transform_2D(x, y)
        return self.transform_perspective(x, y)

    def transform_2D(self, x, y):
        return int(x), int(y)

    def transform_perspective(self, x, y):
        # tr_y: allows the height to be set at the perspective point
        tr_y = y * self.perspective_point_y / self.height
        if tr_y > self.perspective_point_y:
            tr_y = self.perspective_point_y

        diff_x = x - self.perspective_point_x
        diff_y = self.perspective_point_y - tr_y
        offset_x = diff_x * diff_y / self.perspective_point_y
        tr_x = self.perspective_point_x + offset_x
        return int(tr_x), int(tr_y)


class DiamonbackApp(App):
    pass


DiamonbackApp().run()
