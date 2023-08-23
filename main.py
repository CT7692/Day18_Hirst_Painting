import colorgram
from turtle import Turtle, Screen, colormode
import random as r
colormode(255)
def get_colors(color_list, palette):
    for i in palette:
        r = i.rgb.r
        g = i.rgb.g
        b = i.rgb.b
        color_tuple = (r, g, b)
        color_list.append(color_tuple)

def draw_circles(obj, x_pos, y_pos, original_x, color_list):
    obj.up()
    obj.setpos(x_pos, y_pos)
    obj.speed(0)
    for i in range(15):
        for j in range(18):
            obj.down()
            t_clone = obj.clone()
            t_clone.color(r.choice(color_list))
            t_clone.shape("circle")
            x_pos += 50
            obj.up()
            obj.setx(x_pos)
        y_pos += 50
        x_pos = original_x
        obj.setpos(x_pos, y_pos)
    obj.hideturtle()


colors = colorgram.extract('limbo.jpg', 10)
tim = Turtle()
my_screen = Screen()
x = -425
y = -350
colors_extracted = []
get_colors(colors_extracted, colors)
draw_circles(tim, x, y, x, colors_extracted)
my_screen.exitonclick()
