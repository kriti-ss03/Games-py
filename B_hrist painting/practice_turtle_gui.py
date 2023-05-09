import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

timmy=Turtle()
timmy.showturtle()

#  SQUARE
# for i in range(0,4):
#     timmy.fd(100)
#     timmy.right(90)
# #     define angle also

# DASHED LINE
# for i in range(15):
#     timmy.fd(10)
#     timmy.penup()
#     timmy.fd(10)
#     timmy.pendown()

# for i in  range(3,11):
#     # 3 to 10
#     for j in range(0,i):
#         timmy.fd(50)
#         timmy.left(360/i)


# # RANDOM WALK by generating colors(tuple)
def color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

#
# angle=[0,90,180,270]
# timmy.pensize(10)
# timmy.speed("fastest")
#
# for i in range(200):
#     timmy.fd(30)
#     c = color()
#     timmy.pencolor(c)
#     theta=random.choice(angle)
#     timmy.left(theta)


# SPIROGRAPH
timmy.speed("fastest")
# to get diff tilt angles--it has to go 360/n times to make spirograph
theta=random.randint(10,90)
# range needs whole number so int(_) or use //
for i in range (360//theta +1):
    timmy.pencolor(color())
    timmy.circle(50)
    timmy.left(theta)

canvas=Screen()
canvas.exitonclick()