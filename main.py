from turtle import Turtle, Screen
from field import Field
from paddles import Paddle

screen = Screen()
screen.setup(width=1000, height=650)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

field = Field()

player_1 = Paddle((-450, 0))
player_2 = Paddle((450, 0))
screen.tracer(1)

screen.exitonclick()