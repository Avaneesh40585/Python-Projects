from turtle import Turtle
COLOR="azure"
SHAPE="square"
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self): 
        self.body=[]
        self.create_snake()
        self.head=self.body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self,position):
        new_segment=Turtle(shape=SHAPE)
        new_segment.color(COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.body.append(new_segment)
    
    def extend(self):
        self.add_segment(self.body[-1].position())
            
    def move(self,distance=10):
        for seg_num in range(len(self.body)-1,0,-1):
            new_x=self.body[seg_num-1].xcor()
            new_y=self.body[seg_num-1].ycor()
            self.body[seg_num].goto(new_x,new_y)
        self.body[0].forward(distance)
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
    def refresh(self):
        for segment in self.body:
            segment.goto(1000,1000)
            segment.hideturtle()
        self.body.clear()
        self.create_snake()
        self.head=self.body[0]