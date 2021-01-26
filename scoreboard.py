from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("dark blue")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=275)
        self.write("PONG GAME", align="center",
                   font=("Courier", 40, "normal"))
        self.l_score = 0
        self.r_score = 0
        self.goto(x=-200, y=230)
        self.write(f"PLAYER_1 = {self.l_score}", align="center",
                   font=("Courier", 30, "normal"))
        self.goto(x=200, y=230)
        self.write(f"PLAYER_2 = {self.r_score}", align="center",
                   font=("Courier", 30, "normal"))

    def header(self):
        self.goto(x=0, y=275)
        self.write("PONG GAME", align="center",
                   font=("Courier", 40, "normal"))

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.goto(x=-200, y=230)
        self.write(f"PLAYER_1 = {self.l_score}", align="center",
                   font=("Courier", 30, "normal"))
        self.goto(x=200, y=230)
        self.write(f"PLAYER_2 = {self.r_score}", align="center",
                   font=("Courier", 30, "normal"))

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.goto(x=-200, y=230)
        self.write(f"PLAYER_1 = {self.l_score}", align="center",
                   font=("Courier", 30, "normal"))
        self.goto(x=200, y=230)
        self.write(f"PLAYER_2 = {self.r_score}", align="center",
                   font=("Courier", 30, "normal"))
