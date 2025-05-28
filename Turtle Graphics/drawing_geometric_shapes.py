import random
from turtle import Turtle, Screen

# Shapes(triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon).
FULL_ANGLE = 360
COLOURS = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
DISTANCE = 100
tim = Turtle()


def draw_shape(number_of_sides):
    for _ in range(number_of_sides):
        tim.forward(DISTANCE)
        tim.right(FULL_ANGLE / number_of_sides)  # internal angle


for n in range(3, 11):
    tim.color(random.choice(COLOURS))
    tim.width(n)
    draw_shape(n)

screen = Screen()
screen.exitonclick()
