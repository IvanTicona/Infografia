import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Uso de Sprites"

class Mario(arcade.Sprite):
  def __init__(self, image, scale, center_x, center_y):
    super().__init__(image, scale, center_x=center_x, center_y=center_y)
    self.speed = 0

class App(arcade.Window):
  def __init__(self):
    super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.BLACK)

    self.sprites = arcade.SpriteList()
    self.mario = Mario(
      "./img/mario.gif", 
      1, 
      SCREEN_WIDTH//2, 
      SCREEN_HEIGHT//2
    )

    self.sprites.append(self.mario)

  def on_update(self, delta_time: float):
    self.sprites.update()

  def on_draw(self):
    arcade.start_render()
    self.sprites.draw()


if __name__ == "__main__":
  app = App()
  arcade.run()