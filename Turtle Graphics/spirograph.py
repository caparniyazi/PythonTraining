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


def draw_shape():
    while True:
        tim.color(random_color())
        tim.speed(SPEED)
        tim.circle(100)
        tim.setheading(tim.heading() + 10)
        tim.circle(100)


draw_shape()
screen = Screen()
screen.exitonclick()
