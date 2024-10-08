import arcade
import arcade.color
from bresenham import get_line, get_circle
import math

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Primitivas de arcade"


class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size = 10
        
    def on_update(self, delta_time: float):
        pass

    def on_draw(self):
        
        arcade.start_render()
        self.draw_lake()
        self.draw_sky()
        self.draw_sun()
        
        
    def draw_lake(self):
        arcade.draw_lrtb_rectangle_filled(
            0, 
            SCREEN_WIDTH,
            SCREEN_HEIGHT //2,0,
            arcade.color.AQUA
        )
        
    def draw_sky(self):
        arcade.draw_lrtb_rectangle_filled(
            0, 
            SCREEN_WIDTH,
            SCREEN_HEIGHT, 
            SCREEN_HEIGHT // 2,
            arcade.color.RED_DEVIL
        )
        
        
    def draw_sun(self):
        arcade.draw_arc_filled(
            SCREEN_WIDTH//2, SCREEN_HEIGHT//2,
            SCREEN_WIDTH//5, SCREEN_HEIGHT//5,
            arcade.color.YELLOW,
            0,180
        )
        self.draw_rays(0,180,120,50,10, arcade.color.ATOMIC_TANGERINE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
    def draw_rays(self, start_angle, end_angle, d, t, num_rays, color, offset_x=0, offset_y=0):
        angle_step = (end_angle - start_angle) // num_rays 
        sun_radius = SCREEN_WIDTH // 10
        for i in range(num_rays):
            angle_radians = math.radians(start_angle + i * angle_step)
            
            x0 = d * math.cos(angle_radians) + offset_x
            y0 = d * math.sin(angle_radians) + offset_y
            
            x1 = (d + t) * math.cos(angle_radians) + offset_x
            y1 = (d + t) * math.sin(angle_radians) + offset_y
            
            arcade.draw_line(x0,y0,x1,y1,color)
        
    
if __name__ == "__main__":
    app = MyWindow()
    arcade.run()