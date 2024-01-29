from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")
GAME_OVER_FONT = ("Courier", 30, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100,200)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100,200)
        self.write(self.r_score, align="center", font=FONT)
        
    def l_point(self):
        self.l_score += 1
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=FONT)

    def r_point(self):
        self.r_score += 1
        self.goto(100,200)
        self.write(self.r_score, align="center", font=FONT)

    def game_over(self, winner, final_score):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\n{winner} Wins!\nFinal Score: {final_score}", align=ALIGNMENT, font=GAME_OVER_FONT)