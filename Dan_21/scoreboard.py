from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.increase_score()

    
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)
        print(f"{self.score}")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= ALIGNMENT, font = GAME_OVER_FONT)