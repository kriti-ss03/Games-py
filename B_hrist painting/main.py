import turtle
import colorgram
import random
from turtle import Turtle,Screen
turtle.colormode(255)
# install pychaarm preferences->interpre

colors=colorgram.extract('img.jpg',20)

rgb_colors=[]
timmy=Turtle()
timmy.showturtle()

for color in colors:
    r=color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)

for _ in range(10):
    timmy.penup()
    timmy.goto(-60,2*10*_)
    # timmy.setheading()

    for i in range (10):
        color=random.choice(rgb_colors)
        #
        timmy.dot(10,color)
        timmy.penup()
        timmy.fd(20)


print(rgb_colors)

# first_color = colors[0]
# print(first_color)
canvas=Screen()
canvas.exitonclick()