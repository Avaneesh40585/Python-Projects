from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open('data.txt') as high_score_data:
            self.high_score=int(high_score_data.read())
        self.color("gold")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_score()
    
    def refresh(self):
        if(self.score>self.high_score):
            self.high_score=self.score
            with open('data.txt','w') as high_score_data:
                high_score_data.write(f"{self.score}")
        self.score=0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}                High Score: {self.high_score}",align="center",font=("courier",20,"normal"))
    
    def increase_score(self):
        self.score+=1
        self.update_score()
        
    def game_over(self):
        self.color("gold")
        self.goto(0,0)
        self.write(arg=f"Game Over",align="center",font=("courier",50,"normal"))