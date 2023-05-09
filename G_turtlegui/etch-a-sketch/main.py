from turtle import Turtle, Screen

timmy=Turtle()
timmy2=Turtle()

def f():
    timmy.fd(100)

def b():
    timmy.back(100)

def a():
   beta=timmy.heading()
   timmy.setheading(beta+10)
   # timmy.circle(120,40)
def d():
    beta = timmy.heading()
    timmy.setheading(beta - 10)
   # timmy.circle(120,80)

def c():
    timmy.clear()
    timmy.penup()
    timmy.home()
    # timmy.setheading(0)
    # timmy.goto(-10,10)
    timmy.pendown()

screen=Screen()

screen.onkey(fun=f, key ="w")
screen.onkey(fun=b, key ="s")
screen.onkey(fun=a, key ="a")
screen.onkey(fun=d, key ="d")
screen.onkey(fun=c, key ="c")


screen.listen()
screen.exitonclick()