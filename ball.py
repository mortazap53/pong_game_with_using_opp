from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.ball_speed = 0.1
        self.y_steps = 10
        self.x_steps = 10

    def move(self):
        self.setx(self.xcor() + self.x_steps)
        self.sety(self.ycor() + self.y_steps)

    def come_back_y(self):
        self.y_steps *= -1

    def come_back_x(self):
        self.x_steps *= -1
