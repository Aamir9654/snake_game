
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
       
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"score : {self.score} ",align="center",font=("Arial" ,24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Arial" ,24, "normal"))

    def increasescore(self):
        
        self.score +=1
        self.clear()
        self.update_scoreboard()


       
        
        
