from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # default size je 20 x 20, a ako stavimo 0.5 onda je 10x10
        self.speed(0) # ili "fastest"
        self.refresh()


    def refresh(self):
        position_x = random.randrange(0, 280, 20)
        position_y = random.randrange(0, 280, 20)
        self.goto(position_x, position_y)
