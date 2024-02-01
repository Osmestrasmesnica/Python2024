from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        with open("Dan_24/data.txt") as data:
             content = data.read()
             print(content)
        self.high_score = int(content)
        self.score = 0
        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.reset()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align= ALIGNMENT, font = GAME_OVER_FONT)

    def reset(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            with open("Dan_24/data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()