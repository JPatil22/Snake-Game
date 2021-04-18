from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        # self.write(f"Score = {self.score}", align="Center", font=("Ariel", 24, "normal"))
        self.Scorechange()
        self.hideturtle()

    def Scorechange(self):
        self.write(f"Score = {self.score}", align="Center", font=("Ariel", 24, "normal"))

    def Gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="Center", font=("Ariel", 24, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.Scorechange()
