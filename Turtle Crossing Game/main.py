import time
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard

DENSITY=2
counter=0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")

player=Player()
scoreboard=Scoreboard()
cars=[]

screen.listen()
screen.onkey(player.up,"Up")
screen.onkey(player.down,"Down")
screen.onkey(player.left,"Left")
screen.onkey(player.right,"Right")

switch = True
while switch:
    time.sleep(0.1)
    screen.update()
    
    # Car Creation:
    if(counter<=150 and counter%7.5==0):
        for i in range(DENSITY):
            car=Car()
            cars.append(car)
        
    
    # Car movement and respawn:
    for car in cars:
        if(car.xcor()>-350):
            car.move()
        else:
            car.refresh()
    
    # Detect level completion:
    if(player.ycor()>=280):
        scoreboard.level+=1
        scoreboard.update_score()
        for car in cars:
            car.speed_up+=2
        player.refresh()
    
    # Detect collision with cars:
    for car in cars:
        if(car.distance(player)<20):
            scoreboard.game_over()
            switch=False
    counter+=1
    
screen.exitonclick()