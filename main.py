from turtle import Screen
from field import Field
from paddles import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=1000, height=650)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
field_1 = Field()
player_1 = Paddle((-450, 0))
player_2 = Paddle((450, 0))
ball = Ball()
score = Score()


screen.listen()
screen.onkey(player_1.up, "w")
screen.onkey(player_1.down, "s")
screen.onkey(player_2.up, "o")
screen.onkey(player_2.down, "l")

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 305 or ball.ycor() < -305:
        ball.come_back_y()

    if (ball.distance(player_1) < 50 and ball.xcor() < -420
            or ball.distance(player_2) < 50 and ball.xcor() > 420):
        ball.come_back_x()

    if ball.xcor() < -450:
        ball.create_new_ball()
        score.adding_score_1()

    if ball.xcor() > 450:
        ball.create_new_ball()
        score.adding_score_2()

screen.exitonclick()