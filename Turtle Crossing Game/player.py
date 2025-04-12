from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.color("black")
        self.penup()
        self.speed("fastest")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
    def up(self):
        new_y=self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
    
    def down(self):
        new_y=self.ycor()-MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
    
    def right(self):
        new_x=self.xcor()+MOVE_DISTANCE
        self.goto(new_x,self.ycor())
        
    def left(self):
        new_x=self.xcor()-MOVE_DISTANCE
        self.goto(new_x,self.ycor())
        
    def refresh(self):
        self.goto(STARTING_POSITION)
        
    
