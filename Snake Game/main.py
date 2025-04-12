from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

scoreboard=Scoreboard()
food=Food()
snake=Snake()
screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Running the Game:
switch=True
while switch:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect Collision with food:
    if(snake.head.distance(food)<=15):
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    # Detect Collision with walls:
    if(snake.head.xcor()>280 or snake.head.ycor()>260 or snake.head.xcor()<-280 or snake.head.ycor()<-280):
        scoreboard.refresh()
        snake.refresh()
        
        # Game Over Logic:
        # scoreboard.game_over()
        # switch=False
    
    # Detect Collision with body:
    for segment in snake.body:
        if (segment==snake.body[0] or segment==snake.body[1]):
            pass
        elif(snake.head.distance(segment)<10):
            scoreboard.refresh()
            snake.refresh()
            
            # Game Over Logic:
            # switch=False
            # scoreboard.game_over()
            
    # Todo: Ask the user if he wants to continue playing or quit.
screen.exitonclick()