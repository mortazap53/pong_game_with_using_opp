from turtle import Turtle

class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 325)
        while self.xcor() > -325:
            self.setheading(270)
            self.penup()
            self.forward(20)
            self.pendown()
            self.forward(20)