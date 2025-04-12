from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

ball_speed=2

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left_paddle=Paddle((-350,0))
right_paddle=Paddle((350,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(left_paddle.up,"w")
screen.onkey(right_paddle.up,"Up")
screen.onkey(left_paddle.down,"s")
screen.onkey(right_paddle.down,"Down")

switch=True
while switch:
    screen.update()
    ball.forward(ball_speed)
    
    # Detect collision with the wall & Bounce:
    if(ball.ycor()>290 or ball.ycor()<-290):
        ball.wall_bounce()
        if(ball_speed<5):
            ball_speed+=0.5
    
    # Detect the hit:
    if((ball.distance(left_paddle)<=50 and ball.xcor()<-330) or (ball.distance(right_paddle)<=50 and ball.xcor()>330)):
        ball.paddle_bounce()
        if(ball_speed<5):
            ball_speed+=1
    
    # Detect the right miss:
    if(ball.xcor()>400):
        scoreboard.l_score+=1
        scoreboard.update_score()
        ball_speed=2
        ball.refresh()
    
    # Detect the left miss:
    if(ball.xcor()<-400):
        scoreboard.r_score+=1
        scoreboard.update_score()
        ball_speed=2
        ball.refresh()
        
screen.exitonclick()