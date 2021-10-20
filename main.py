# import colorgram

# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

import turtle as t
import random

start_pos_x = 0
start_pos_y = 0
space = 50
dot_size = 20
columns = 10
rows = 10
color_list = [(131, 165, 206), (225, 151, 100), (32, 41, 59), (200, 134, 147), (235, 212, 87), (166, 56, 46),
              (39, 104, 153), (141, 184, 161), (153, 58, 65), (170, 29, 33), (217, 80, 69), (158, 32, 29), (15, 96, 71),
              (236, 165, 156), (50, 111, 90), (58, 50, 47), (50, 42, 46), (228, 164, 168), (34, 61, 56),
              (170, 188, 222), (190, 99, 108), (32, 59, 108), (103, 127, 163), (34, 151, 210), (175, 200, 188),
              (66, 66, 56)]

tim = t.Turtle()
tim.speed(0)
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
(start_pos_x, start_pos_y) = tim.position()
t.colormode(255)

def draw_dotted_line():
    tim.pendown()
    tim.dot(dot_size, random.choice(color_list))
    tim.penup()
    tim.forward(50)


for i in range(0, columns):
    tim.setposition(start_pos_x, start_pos_y + 50*i)
    for _ in range(rows):
        draw_dotted_line()

tim.hideturtle()

screen = t.Screen()
screen.exitonclick()
