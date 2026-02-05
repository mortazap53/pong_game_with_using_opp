from turtle import Screen
from field import Field
from paddles import Paddle

screen = Screen()
screen.setup(width=1000, height=650)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
field_1 = Field()
player_1 = Paddle((-450, 0))
player_2 = Paddle((450, 0))
screen.tracer(1)

screen.listen()
screen.onkey(player_1.up, "w")
screen.onkey(player_1.down, "s")
screen.onkey(player_2.up, "o")
screen.onkey(player_2.down, "l")

screen.exitonclick()