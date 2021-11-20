import turtle as t
import random
import colorgram
import pyautogui


# get the location of the image
file_path = input("Enter file path of image: ")
user_func = input("Enter a linear function: ")
step_width = int(input("Enter a step width: "))
backgroundColor = (int(x) for x in input("Background rgb Color: ").split())
# extract colors form image and store it in a list
colors = colorgram.extract(file_path, 30)
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
tim.forward(200)
tim.setheading(0)
(start_pos_x, start_pos_y) = tim.position()
t.colormode(255)

# get the special function of the user
def f(x):
    f = eval(user_func)
    return f

# drawing function: draws dots
def draw_dotted_line(x, y):
    tim.goto(x, y + f(x))
    tim.pendown()
    tim.dot(dot_size, random.choice(rgb_colors))
    tim.penup()

# actual drawing happens here
for i in range(0, columns):
    for j in range(rows):
        draw_dotted_line(start_pos_x + step_width * j, start_pos_y + step_width * i)

# hides the turtle
tim.hideturtle()

# setting up screen size
screen = t.Screen()
screen.setup(width=1.0, height=1.0, startx=None, starty=None)
screen.bgcolor(backgroundColor)


# takes a screenshot of the window
myscreenshot = pyautogui.screenshot()
myscreenshot.save('/Users/riccardofeingold/Downloads/screenshot.png')
# (optional) send you the image on to your phone

screen.exitonclick()
