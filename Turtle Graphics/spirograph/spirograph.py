import random
import turtle
from turtle import Turtle, Screen

DISTANCE = 30
SPEED = "fastest"
tim = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def draw_shape(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.speed(SPEED)
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_shape(5)

screen = Screen()
screen.exitonclick()
