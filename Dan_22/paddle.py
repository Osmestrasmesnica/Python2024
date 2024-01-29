from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, initial_x):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # Adjusted size for better appearance
        self.penup()
        self.goto(initial_x, 0)
        self.speed(0)

    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)