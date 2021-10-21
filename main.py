import turtle as t
import random
import colorgram

# get the location of the image
file_path = input("Enter file path of image: ")

# extract colors form image and store it in a list
colors = colorgram.extract('image.jpg', 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color = (r, g, b)
    rgb_colors.append(new_color)

# initializing values for drawing
start_pos_x = 0
start_pos_y = 0
space = 50
dot_size = 20
columns = 10
rows = 10

# setting up my drawing robot
tim = t.Turtle()
tim.speed(0)
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
(start_pos_x, start_pos_y) = tim.position()
t.colormode(255)

# drawing function: draws dots
def draw_dotted_line():
    tim.pendown()
    tim.dot(dot_size, random.choice(rgb_colors))
    tim.penup()
    tim.forward(50)

# actual drawing happens here
for i in range(0, columns):
    tim.setposition(start_pos_x, start_pos_y + 50*i)
    for _ in range(rows):
        draw_dotted_line()

# hides the turtle
tim.hideturtle()

# takes a screenshot of the window

# (optional) send you the image on to your phone

screen = t.Screen()
screen.exitonclick()
