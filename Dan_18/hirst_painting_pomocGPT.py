import turtle as t
from turtle import Screen, Turtle
import random

color_list = [
    (198, 13, 32),
    (248, 236, 25),
    (40, 76, 188),
    (39, 216, 69),
    (238, 227, 5),
    (227, 159, 49),
    (29, 40, 154),
    (212, 76, 15),
    (17, 153, 17),
    (241, 36, 161),
    (195, 16, 12),
    (223, 21, 120),
    (68, 10, 31),
    (61, 15, 8),
    (223, 141, 206),
    (11, 97, 62),
    (219, 159, 11),
    (54, 209, 229),
    (19, 21, 49),
    (238, 157, 216),
    (79, 74, 212),
    (10, 228, 238),
    (73, 212, 168),
    (93, 233, 198),
    (65, 231, 239),
    (217, 88, 51),
]

ori = Turtle()
t.colormode(255)
ori.shape('turtle')
ori.color("dark green")
ori.resizemode("auto")
ori.speed(0)

# Set initial position on the left side
ori.penup()
ori.setpos(-200, 300)
ori.pendown()

def circle():
    ori.dot(20, random.choice(color_list))
    ori.penup()
    ori.forward(50)
    ori.pendown()

def row_circles():
    for i in range(10):
        circle()
    
    # Move to the next row
    ori.penup()
    ori.setx(-200)  # Move back to the start of the row
    ori.sety(ori.ycor() - 50)  # Move down by 50 units
    ori.pendown()

# Move the turtle to the starting position
ori.penup()
ori.setpos(-200, 300)
ori.pendown()

for j in range(10):
    row_circles()

# Create the screen
screen = Screen()
# Exit on click
screen.exitonclick()
