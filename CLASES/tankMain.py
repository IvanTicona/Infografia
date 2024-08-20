import arcade 
from game_object import Polygon2D


class App(arcade.Window):
  def __init__(self):
    super().__init__(800, 800, "Polygon 2D")
    arcade.set_background_color(arcade.color.BLACK)
    self.objects = []

  def on_key_release(self, symbol: int, modifiers: int):
    if symbol == arcade.key.UP:
      self.tank.speed = SPEED
    elif symbol == arcade.key.DOWN:
      self.tank.speed = -SPEED

  def on_mouse_release(self, x, y, button, modifiers):
    if button == arcade.MOUSE_BUTTON_LEFT:
      self.objects.append(
        Polygon2D(
          vertices=[
            (x-50, y-50),
            (x-50, y+50),
            (x+50, y+50),
            (x+50, y-50),
          ],
          color=(255, 0, 0),
        )
      )

  def on_draw(self):
    arcade.start_render()
    for obj in self.objects:
      obj.draw()

  def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
    pass

  def on_update(self, delta_time: float):
    pass