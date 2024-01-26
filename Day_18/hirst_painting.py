#! ovo smo koristili da extraktujemo boje iz slike
# import colorgram

# colors = colorgram.extract('../image.jpg', 30)
# first_color = colors[0]
# rgb_first_color = first_color.rgb
# # print(colors)

# list_of_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     list_of_colors.append(new_color)

# print(list_of_colors)


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

# 10 x 10 kruzica, velicine 20, a razmaka 50

import random
import turtle as t
from turtle import Screen, Turtle

ori = Turtle()
t.colormode(255)
ori.shape('turtle')
ori.color("dark green")
ori.resizemode("auto")
ori.speed(0)
a = 0
b = 0

def circle():
    ori.dot(20, random.choice(color_list))
    ori.penup()
    ori.forward(50)
    ori.pendown()

def row_circles():
    global b
    for i in range(10):
        circle()    
    ori.teleport(a, b+50)
    b += 50

for j in range(10):
    row_circles()

# napravi ekran
screen = Screen()
# izlazi ako kliknes sa strane
screen.exitonclick()