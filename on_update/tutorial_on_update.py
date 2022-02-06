import arcade


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)

        self.c_x = 200
        self.c_y = arcade.get_window().height/2
        self.raggio = 50
        self.x_speed = 300

        self.set_location(400, 200)
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.c_x, self.c_y, self.raggio, arcade.color.RED, 0, 100)

    def on_update(self, delta_time: float):
        self.c_x += self.x_speed * delta_time

        if self.c_x <= 10+self.raggio or self.c_x >= arcade.get_window().width-self.raggio:
            self.x_speed *= -1

MyGameWindow(1280, 720, 'Il mio gioco')

arcade.run()