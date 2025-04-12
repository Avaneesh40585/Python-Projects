from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-265,265)
        self.level=1
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Level = {self.level}",align="left",font=("Courier", 24, "normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Courier", 80, "normal"))
        
