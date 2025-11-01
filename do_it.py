

import colorgram
from turtle import Turtle, Screen, colormode
import random

# Allow using RGB color tuples (0-255)
colormode(255)

# Color list extracted using colorgram (you already have it):
s_colors = [(248, 228, 240), (245, 212, 197), (129, 87, 69), (199, 147, 126), (50, 33, 25), (21, 31, 60), (168, 113, 95), (230, 178, 161), (195, 145, 159), (227, 227, 241)]
tim = Turtle()
tim.shape("turtle")
tim.penup()
tim.speed("fastest")

# Move to starting corner
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

# Draw 10x10 grid of dots
for row in range(10):
    for col in range(10):
        tim.color(random.choice(s_colors))
        tim.dot(20)
        tim.forward(50)

    # Move to next row
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(50 * 10)
    tim.setheading(0)

screen = Screen()
screen.exitonclick()
