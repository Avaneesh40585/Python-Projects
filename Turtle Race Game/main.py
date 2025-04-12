from turtle import Turtle,Screen
from random import randint
switch=False
colors=["pink","black","grey","blue","green","yellow","orange","red"]
screen=Screen()
screen.title("Turtle Race")
screen.setup(height=500,width=750)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Choose a color: (pink/black/grey/blue/green/yellow/orange/red)")
turtles=[]

for i in range(len(colors)):
    turtle=Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-350,y=50*i-175)
    turtles.append(turtle)

if user_bet:
    switch=True

while switch:
    for turtle in turtles:
        if turtle.xcor()>355:
            switch=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! {winning_color} turtle is the winner")
            else:
                print(f"You've lost! {winning_color} turtle is the winner")
        random_distance=randint(0,20)
        turtle.forward(random_distance)
        
screen.exitonclick()