import arcade
from bresenham import get_line, get_circle

class MyWindow(arcade.Window):
  def __init__ (self):
    self.vertices = [(100, 100), (200, 200), (200, 100), (100, 200)]

  def on_update(self, delta_time: float):
    pass

  def on_draw(self):
    arcade.start_render()
    self.draw_shapes(self.vertices)

  def draw_shapes(self):
    for x, y in self.vertices:
      arcade.draw_point(x, y, arcade.color.WHITE, 5)
    arcade.draw_line(100, 100, 200, 200, arcade.color.WHITE)

  def translate(self, vertices, dx, dy):
    return [(x + dx, y + dy) for x, y in vertices] #List comprehension


if __name__ == "__main__":
  app = MyWindow()
  arcade.run()