import arcade
import pymunk
from game_object import Box

WIDTH = 800
HEIGHT = 800
TITLE = "boxes"

class App(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        # Crear espacio
        self.space = pymunk.Space()
        self.space.gravity = (0, -500)  # Aumentar la gravedad para que sea más evidente

        # Crear piso
        self.create_ramps()

        # Sprites
        self.sprites = arcade.SpriteList()
        self.sprites.append(Box(750, 600, self.space))
        self.sprites.append(Box(750, 650, self.space))
        self.sprites.append(Box(650, 600, self.space))
        self.sprites.append(Box(650, 650, self.space))
        self.sprites.append(Box(100, 500, self.space))
        self.sprites.append(Box(150, 500, self.space))
        self.sprites.append(Box(200, 500, self.space))

    def create_ramps(self):
        # Rampa 1 debajo de 4 sprites
        ramp1_start = (600, 480)
        ramp1_end = (800, 560)
        ramp1 = pymunk.Segment(self.space.static_body, ramp1_start, ramp1_end, 1)
        ramp1.friction = 1.0
        self.space.add(ramp1)

        # Rampa 2 debajo de 3 sprites
        ramp2_start = (50, 480)
        ramp2_end = (250, 360)
        ramp2 = pymunk.Segment(self.space.static_body, ramp2_start, ramp2_end, 1)
        ramp2.friction = 1.0
        self.space.add(ramp2)

    def on_update(self, delta_time: float):
        self.space.step(1 / 60)
        self.sprites.update()

    def on_draw(self):
        arcade.start_render()
        self.sprites.draw()
        arcade.draw_line(600, 480, 800, 560, arcade.color.WHITE, 2)
        arcade.draw_line(50, 480, 250, 360, arcade.color.WHITE, 2)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.sprites.append(Box(x, y, self.space))


if __name__ == "__main__":
    app = App()
    arcade.run()


