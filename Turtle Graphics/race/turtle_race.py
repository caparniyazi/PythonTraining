import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False


def create_turtle(color, x_pos, y_pos):
    the_turtle = Turtle(shape="turtle")
    the_turtle.penup()
    the_turtle.shape()
    the_turtle.color(color)
    the_turtle.goto(x=x_pos, y=y_pos)

    return the_turtle


all_turtles = []
y = -100
for i in range(0, 6):
    new_turtle = create_turtle(colors[i], x_pos=-230, y_pos=y)
    y += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)  # The random distance the turtle is going to move forward.
        turtle.forward(random_distance)

screen.exitonclick()
