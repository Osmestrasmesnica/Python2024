from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.goto(-200, 275)
        self.write(f"Trenutni nivo: {self.score}", align="center", font=FONT)
        
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\nHigh Score:{self.score}", align="center", font=FONT)

