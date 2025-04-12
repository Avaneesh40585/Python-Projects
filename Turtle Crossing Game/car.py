from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 4

class Car(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.penup()
        self.setheading(180)
        self.speed("fastest")
        self.goto(random.randint(280,300),random.randint(-220,250))
        self.speed_up=STARTING_MOVE_DISTANCE
    
    def move(self):
        self.forward(self.speed_up)
    
    def refresh(self):
        self.goto(random.randint(300,330),random.randint(-220,250))
            
            
    
