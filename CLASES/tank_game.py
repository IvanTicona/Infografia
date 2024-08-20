

class Tank:
  def __init__(self, x, y, width, height, color):
    self.x = x
    self.y = y
    self.speed = 0
    self.angular_speed = 0
    self.theta = 0
    self.body = Polygon2D(
      vertices=[
        (x-width//2, y-height//2),
        (x-width//2, y+height//2),
        (x+width//2, y+height//2),
        (x+width//2, y-height//2),
      ],
      color=color,
    )

  def update(self, delta_time: float):
    dtheta = self.angular_speed * delta_time
    dx = self.speed * math.cos(self.theta) * delta_time
    dy = self.speed * math.sin(self.theta) * delta_time

    #apply transforms
    self.body.translate(dx, dy)
    self.body.rotate(dtheta, pivot=(self.x, self.y))
    #update tank state
    self.theta += dtheta
    self.x += dx
    self.y += dy

  def draw(self):
    self.body.draw()