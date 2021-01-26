from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=900, height=700)
screen.bgcolor("orange")
screen.tracer(0)

r_paddle = Paddle(position_of_paddle=(400, 0))
l_paddle = Paddle(position_of_paddle=(-400, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting Collision with the wall.
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()

    # Detecting Collision with the paddle.
    if ball.distance(r_paddle) < 75 and ball.xcor() > 370:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 75 and ball.xcor() < -370:
        ball.bounce_x()

    # Detecting Collision when the r_paddle misses.
    if ball.xcor() > 430:
        ball.reset_position()
        ball.bounce_x()
        score.l_point()
        score.header()

    # Detecting Collision when the l_paddle misses.
    if ball.xcor() < -430:
        ball.reset_position()
        ball.bounce_x()
        score.r_point()
        score.header()


screen.exitonclick()
