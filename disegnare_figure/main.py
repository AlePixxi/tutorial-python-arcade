import arcade


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)

        self.c_x = 200
        self.c_y = 200
        self.raggio = 50

        self.set_location(400, 200)
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_xywh_rectangle_filled(0, 0, arcade.get_window().width, arcade.get_window().height/2,
                                          arcade.color.DARK_GREEN)

        arcade.draw_triangle_filled(0, arcade.get_window().height/2,
                                    300, arcade.get_window().height/2 + 100,
                                    600, arcade.get_window().height/2, arcade.color.DARK_BROWN)

        arcade.draw_triangle_filled(600, arcade.get_window().height / 2,
                                    900, arcade.get_window().height / 2 + 100,
                                    1200, arcade.get_window().height / 2, arcade.color.DARK_BROWN)

        arcade.draw_circle_filled(100, arcade.get_window().height - self.raggio-80, self.raggio, arcade.color.YELLOW,
                                  0, 100)


MyGameWindow(1280, 720, 'Il mio gioco')
print(arcade.get_window().width)

arcade.run()
