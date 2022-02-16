import arcade


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)

        self.set_location(400, 200)
        arcade.set_background_color(arcade.color.SPACE_CADET)
        self.mia_sprite = arcade.Sprite(arcade.resources.image_player_ship1_green, center_x=100, center_y=100)

        self.c_x = 200
        self.c_y = 200

        self.speed = .1

        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def on_draw(self):
        arcade.start_render()
        self.mia_sprite.draw()

    def on_update(self, delta_time):
        if self.up: self.mia_sprite.strafe(self.speed)
        if self.down: self.mia_sprite.strafe(-self.speed)

        if self.right: self.mia_sprite.turn_right(2)
        if self.left: self.mia_sprite.turn_left(2)

        self.mia_sprite.update()

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


GameWindow(1280, 720, 'Il mio gioco')
arcade.run()
