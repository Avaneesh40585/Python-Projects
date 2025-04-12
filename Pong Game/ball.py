from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("red")
        self.penup()
        self.setheading(random.randint(0,360))
        
    # def move(self,distance=3):
    #     self.forward(distance)
        # new_xcor=self.xcor()+distance
        # new_ycor=self.ycor()+distance
        # self.goto(new_xcor,new_ycor)
        
    def wall_bounce(self):
        if(self.ycor()>0):
            self.setheading(-self.heading())
        elif(self.ycor()<0):
            self.setheading(360-self.heading())
    
    def paddle_bounce(self):
        if(self.ycor()<0 and self.xcor()>0):
            self.setheading(540-self.heading())
        else:
            self.setheading(180-self.heading())
    
    def refresh(self):
        self.goto(0,0)
        self.setheading(random.randint(0,360))
        