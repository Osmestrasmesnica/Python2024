#! PYTHON DAN 18
#! Turtle module, nastavak
import turtle as t
from turtle import Screen, Turtle
import random

ori = Turtle()
t.colormode(255)
ori.shape('turtle')
#ori_kornjaca.register_shape("anka.gif")
ori.color("dark green")

# # slovo A
# ori_kornjaca.left(90)
# ori_kornjaca.forward(100)
# ori_kornjaca.right(90)
# ori_kornjaca.forward(50)
# ori_kornjaca.right(90)
# ori_kornjaca.forward(50)
# ori_kornjaca.right(90)
# ori_kornjaca.forward(50)
# ori_kornjaca.right(180)
# ori_kornjaca.forward(50)
# ori_kornjaca.right(90)
# ori_kornjaca.forward(50)

# napravi kvadrat 100x100

# for _ in range(4):
#     ori.forward(100)
#     ori.right(90)

#! importovanje svega iz modula sa "*"
#from turtle import *

#! dodaj importovano modulu novo ime sa "as"
# import turtle as t
# leka = t.Turtle()

#! neki modeli moraju da se instaliraju preko python packages
# import heros


# #! Nacrtaj isprekidanu liniju, 10 nacrtanih pa 10 praznih jedinica
# for _ in range(15):
#     ori.forward(10)
#     ori.penup()
#     ori.forward(10)
#     ori.pendown()

#! nacrtaj trougao, kvadrat, pentagon, hexagon, heptagon, octagon, nanogon i decagon
# full_circle = 360

# for _ in range (3):
#     ori.forward(100)
#     ori.right(full_circle/(3))
# for _ in range (4):
#     ori.forward(100)
#     ori.right(full_circle/(4))
# for _ in range (5):
#     ori.forward(100)
#     ori.right(full_circle/(5))
# for _ in range (6):
#     ori.forward(100)
#     ori.right(full_circle/(6))
# for _ in range (7):
#     ori.forward(100)
#     ori.right(full_circle/(7))
# for _ in range (8):
#     ori.forward(100)
#     ori.right(full_circle/(8))
# for _ in range (9):
#     ori.forward(100)
#     ori.right(full_circle/(9))
# for _ in range (10):
#     ori.forward(100)
#     ori.right(full_circle/(10))

# #? bolji kod isto radi kao ovaj iznad
# color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateGray", "SeaGreen", "Pink", "Purple", "Red"]

# number_of_sides = 0
# full_circle = 360
# def draw_shape(number_of_sides):
#     for _ in range (number_of_sides):
#         ori.forward(100)
#         ori.right(full_circle/number_of_sides)

# for i in range(2,10):
#     ori.color(random.choice(color))
#     number_of_sides = i+1
#     draw_shape(number_of_sides)

# #! Generisati random walk, iste duzine, i boja da je random
# #? Aleksino resenje, radi
# color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateGray", "SeaGreen", "Pink", "Purple", "Red"]
# x = 0
# ori.speed(0)
# while x < 200:
#     i = random.randint(1,4)
#     ori.left(90*i)
#     ori.forward(50)
#     ori.color(random.choice(color))
#     x+=1

# #? Resenje kurs
# color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateGray", "SeaGreen", "Pink", "Purple", "Red"]
# direction = [0, 90, 180, 270]
# ori.pensize(5)
# ori.speed(0)
# ori.resizemode("auto")
# for _ in range(200):
#     ori.color(random.choice(color))
#     ori.setheading(random.choice(direction))
#     ori.forward(30)
    
# #! kako napraviti random boju skroz a ne listu boja
# #RGB red green blue (1, 3, 8)
# # ne moze da se menja npr my_tuple[2] = 12
# # ali moze ovako

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)


# direction = [0, 90, 180, 270]
# ori.pensize(5)
# ori.speed(0)
# ori.resizemode("auto")
# for _ in range(200):
#     ori.color(random_color())
#     ori.setheading(random.choice(direction))
#     ori.forward(30)

# #! Nacrtaj Spirograph (krugove)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

# ori.speed(0)

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         ori.color(random_color())
#         ori.circle(100)
#         ori.setheading(ori.heading() + 10)


# draw_spirograph(5)



# napravi ekran
screen = Screen()
# izlazi ako kliknes sa strane
screen.exitonclick()