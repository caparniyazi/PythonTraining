from tkinter.constants import CENTER
from turtle import Turtle

FONT = ("Courier", 12, "normal")


def read_score():
    with open("data.txt") as f:
        return int(f.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=CENTER, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score()

        # Reset the score
        self.score = 0
        self.update_scoreboard()

    def inc(self):
        self.score += 1
        self.update_scoreboard()

    def write_score(self):
        with open("data.txt", "w") as f:
            f.write(f"{self.high_score}")
