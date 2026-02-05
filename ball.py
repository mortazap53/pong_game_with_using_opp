from turtle import Turtle

y_steps = 10
x_steps = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.ball_speed = 0.1

    def move(self):
        self.setx(self.xcor() + x_steps)
        self.sety( self.ycor() + y_steps )
