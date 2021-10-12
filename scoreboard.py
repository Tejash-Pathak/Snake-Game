from turtle import *


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        self.high_score = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.update_score()
    def update_score(self):

        self.write(arg=f"Score : {self.score}, High score : {self.high_score}",  align="center", font=("Times new roman", 24, "normal"))
    def reset_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.update_score()
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()