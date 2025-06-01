import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # Get the animations turn off.

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")  # Left paddle up key.
screen.onkey(fun=l_paddle.go_down, key="s")  # Left paddle down key.

game_is_no = True
while game_is_no:
    time.sleep(ball.move_speed)
    screen.update()  # Show the screen.
    ball.move()

    # Detect collision with the wall.

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle.
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when the right paddle misses.
    if ball.xcor() > 380:
        scoreboard.inc_l_point()
        ball.reset()

    # Detect when the left paddle misses.
    if ball.xcor() < -380:
        scoreboard.inc_r_point()
        ball.reset()

screen.exitonclick()
