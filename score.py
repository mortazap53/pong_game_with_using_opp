from turtle import Turtle

Alignment = "center"
Font = ("Courier", 60, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.tracking_score()

    def tracking_score(self):
        self.goto(-80, 250)
        self.write(f"{self.score_1}", align=Alignment, font=Font)
        self.goto(80, 250)
        self.write(f"{self.score_2}", align=Alignment, font=Font)

    def adding_score_1(self):
        self.clear()
        self.score_2 += 1
        self.tracking_score()

    def adding_score_2(self):
        self.clear()
        self.score_1 += 1
        self.tracking_score()
