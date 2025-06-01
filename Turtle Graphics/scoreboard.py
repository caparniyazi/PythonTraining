from tkinter.constants import CENTER
from turtle import Turtle

FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", True, align=CENTER, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, align=CENTER, font=FONT)

    def inc(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
