import arcade


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)

        self.c_x = 200
        self.c_y = 200
        self.raggio = 50
        self.speed = 200

        self.pointer_x = 0
        self.pointer_y = 0

        self.up = False
        self.down = False
        self.left = False
        self.right = False

        self.set_location(400, 200)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.c_x, self.c_y, self.raggio, arcade.color.RED, 0, 100)
        arcade.draw_circle_outline(self.pointer_x, self.pointer_y, self.raggio+2, arcade.color.WHITE, 2, 0, 100)

    def on_update(self, delta_time):
        if self.up: self.c_y += self.speed * delta_time
        if self.down: self.c_y -= self.speed * delta_time

        if self.right: self.c_x += self.speed * delta_time
        if self.left: self.c_x -= self.speed * delta_time

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP: self.up = True
        if symbol == arcade.key.DOWN: self.down = True

        if symbol == arcade.key.RIGHT: self.right = True
        if symbol == arcade.key.LEFT: self.left = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP: self.up = False
        if symbol == arcade.key.DOWN: self.down = False

        if symbol == arcade.key.RIGHT: self.right = False
        if symbol == arcade.key.LEFT: self.left = False

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.c_x = x
            self.c_y = y
    def on_mouse_motion(self, x, y, dx, dy):
        self.pointer_x = x
        self.pointer_y = y



MyGameWindow(1280, 720, 'Il mio gioco')

arcade.run()
