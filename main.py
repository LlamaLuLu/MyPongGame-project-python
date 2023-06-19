# 19/6/2023

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from center_line import Line
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)  # animation off

r_paddle = Paddle((350, 0), "medium purple")  # idea: customise paddle colours
l_paddle = Paddle((-350, 0), "cornflower blue")
line = Line()
ball = Ball()  # idea: change ball colour with speed increase
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect top/bottom wall collision
    if not (-280 < ball.ycor() < 285):
        ball.bounce_y()

    # detect paddle collision
    if (ball.distance(r_paddle) < 65) or (ball.distance(l_paddle) < 65):
        if (ball.xcor() > 325) or (ball.xcor() < -325):
            ball.bounce_x()

    # detect R paddle miss
    if ball.xcor() > 380:
        scoreboard.l_point()
        time.sleep(0.5)
        ball.reset()

    # detect L paddle miss:
    if ball.xcor() < -390:
        scoreboard.r_point()
        time.sleep(0.5)
        ball.reset()

screen.exitonclick()
