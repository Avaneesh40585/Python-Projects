from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.left_score()
        self.right_score()
        
    def left_score(self):
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("Pixel Sport",60,"normal"))
        
    def right_score(self):
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("Pixel Sport",60,"normal"))
        