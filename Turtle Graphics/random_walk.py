import random
import turtle
from turtle import Turtle, Screen

DISTANCE = 30
DIRECTIONS = [0, 90, 180, 270]
PEN_SIZE = 15
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
        tim.width(PEN_SIZE)
        tim.forward(DISTANCE)
        tim.setheading(random.choice(DIRECTIONS))


draw_shape()
screen = Screen()
screen.exitonclick()
