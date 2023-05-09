from turtle import Turtle, Screen
import random


screen=Screen()
user_bet=screen.textinput(title="Make your bet",prompt="who will win? ")
screen.setup(width=500,height=400)

is_raceOn=False
# list of obejct of class TURTLE--store multiple objects
allturtles=[]
colours=["red","green","blue","yellow","brown"]
ycors=[-100,-50,0,50,100]

if user_bet:
    is_raceOn=True

for i in range(0, 5):
    t = Turtle(shape="turtle")
    t.color(colours[i])
    t.penup()
    t.goto(-230, ycors[i])
    allturtles.append(t)


while is_raceOn:
    for item in allturtles:
        randmove = random.randint(1, 10)
        item.forward(randmove)
        dis=item.xcor()
        # method!!! xcor()
        # 250-40/2 to see turtle
        if dis > 230:
            win=item.pencolor()
            is_raceOn=False
            if user_bet==win:
                print("you won")
            else:
                print(f"you lose! winner is {win}")



# t1=Turtle(shape="turtle")
# t2=Turtle(shape="turtle")
# t3=Turtle(shape="turtle")
#
# t1.color("red")
# t2.color("blue")
# t3.color("green")

# t1.penup()
# t2.penup()
# t3.penup()
#
# t1.goto(-230,50)
# t2.goto(-230,0)
# t3.goto(-230,-50)

# def randmove(t):
#     arr=[5,10,15,20,25]
#     t.fd(random.choice(arr))
#     return int(t.xcor())

# dis=0
# while(dis!=230):
#     d1=randmove(t1)
#     d2=randmove(t2)
#     d3=randmove(t3)
#     dis=max(d1,max(d2,d3))


screen.exitonclick()
