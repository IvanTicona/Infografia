import arcade


SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Polygon 2D"

def get_random_color():
  return (
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
  )


class App(arcade.Window):
  def __init__(self):
    super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.BLACK)
    self.objects = []

  def on_key_release(self, symbol: int, modifiers: int):
    if symbol == arcade.key.UP:
      for obj in self.objects:
        obj.scale(1.1, 1.1)
    elif symbol == arcade.key.DOWN:
      for obj in self.objects:
        obj.scale(0.9, 0.9)

  def on_mouse_release(self, x, y, button, modifiers):
    if symbol == arcade.key.C:
      self.objects.append(
        Polygon2D(
          vertices=[
            (SCREEN_WIDTH//2-50, SCREEN_HEIGHT//2-50),
            (SCREEN_WIDTH//2-50, SCREEN_HEIGHT//2+50),
            (SCREEN_WIDTH//2+50, SCREEN_HEIGHT//2+50),
            (SCREEN_WIDTH//2+50, SCREEN_HEIGHT//2-50),
          ],
          color=get_random_color(),
        )
      )
      # print(f"objetos len(self.objects)")

  def on_draw(self):
    arcade.start_render()
    for obj in self.objects:
      obj.draw()

  def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
    pass

  def on_update(self, delta_time: float):
    pass

def main():
  window = App()
  arcade.run()