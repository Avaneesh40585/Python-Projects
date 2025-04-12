from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__(shape="square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(position)
    
    def up(self,distance=30):
        new_y=self.ycor()+distance
        self.goto(self.xcor(),new_y)
    
    def down(self,distance=30):
        new_y=self.ycor()-distance
        self.goto(self.xcor(),new_y)