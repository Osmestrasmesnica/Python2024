# #! PYTHON DAN 19
# #! Instances, State and Higher Order Functions

# from turtle import Turtle, Screen

# ori = Turtle()

# screen = Screen()

# # da pocnes da slusas event, onda unosis listen()
# # funkcija da bindujemo dugme da se desi nesto kada se prepozna dugme
# def move_forwards():
#     ori.forward(10)

# screen.listen()
# screen.onkey(key = "Up", fun = move_forwards)  #! --> u ovom slucaju se ne stavljaju () posle funkcije!!!!
# screen.exitonclick()

#! Zadatak 1
# # NAPRAVITI ETCH A SKETCH

# # w = move_forwards
# # s = move_backwards
# # a = counter-clockwise
# # d = clockwise
# # c = clear_drawing and place_at_center

# from turtle import Turtle, Screen
# import random
# ori = Turtle()
# screen = Screen()
# screen.addshape('Dan_19/aleksinaanka.gif')  # Assuming both main.py and a.gif are in the same folder
# screen.addshape('Dan_19/anka1.gif')  # Assuming both main.py and a.gif are in the same folder
# screen.addshape('Dan_19/anka2.gif')  # Assuming both main.py and a.gif are in the same folder
# # ori.shape('Dan_19/aleksinaanka.gif')
# # ori.shape('Dan_19/anka1.gif')
# ori.shape('Dan_19/anka2.gif')
# ori.shapesize(90,90)
# ori.pensize("5")
# ori.speed(0)

# def move_forwards():
#     ori.forward(10)

# def move_backwards():
#     ori.backward(10)

# def counter_clockwise():
#     angle = ori.heading() + 10
#     ori.setheading(angle)

# def clockwise():
#     angle = ori.heading() - 10
#     ori.setheading(angle)

# def clear():
#     ori.clear()
#     ori.penup()
#     ori.home()
#     ori.pendown()

# # list_for_screen_saver = [1, 2, 3, 4]

# # for i in range(500):
# #     random_choice = random.choice(list_for_screen_saver)
# #     if random_choice == 1:
# #         move_forwards()
# #     elif random_choice == 2:
# #         move_backwards()
# #     elif random_choice == 3:
# #         counter_clockwise()
# #     elif random_choice == 4:
# #         clockwise()

# screen.listen()

# screen.onkey(key = "w", fun = move_forwards)
# screen.onkey(key = "s", fun = move_backwards)
# screen.onkey(key = "a", fun = counter_clockwise)
# screen.onkey(key = "d", fun = clockwise )
# screen.onkey(key = "c", fun = clear)

# screen.exitonclick()

#! Object state and Instances

from turtle import Turtle, Screen
import random

screen = Screen()



ori = Turtle(shape = 'turtle')
anka = Turtle(shape = 'turtle')
aleksa = Turtle(shape = 'turtle')
vuk = Turtle(shape = 'turtle')
srna = Turtle(shape = 'turtle')
marija = Turtle(shape = 'turtle')
gif = Turtle()
screen.addshape('Dan_19/aleksinaanka.gif')  # Assuming both main.py and a.gif are in the same folder
gif.shape('Dan_19/aleksinaanka.gif')
# gif.pensize("5")
gif.speed(0)

#different STATE of different objects, different attributes
ori.color('black')
anka.color('yellow')
aleksa.color('purple')
vuk.color('dark green')
srna.color('dark orange')
gif.color('red')
marija.color('blue')



screen.setup(width = 500, height = 400)

# popup izabrati boje
aj_se_kladimo = screen.textinput(title="Koja kornjaca ce da pobedi?", prompt="Na koju kornjacu se kladis? \nUnesi boju: black, yellow, purple, dark green, dark orange, red, blue ")
print(aj_se_kladimo)

# podigni pen da ne crtaju pre nego sto odu sa goto()
ori.penup()
anka.penup()
aleksa.penup()
vuk.penup() 
srna.penup()
gif.penup()
marija.penup()

# poredja ih koristeci goto()
marija.goto(x= -230, y = -180)
ori.goto(x= -230, y = -120)
anka.goto(x= -230, y = -60)
gif.goto(x= -230, y =0)
vuk.goto(x= -230, y = 60)
srna.goto(x= -230, y = 120)
aleksa.goto(x= -230, y = 180)

sve_kornjace = [ori, anka, aleksa, vuk, srna, marija, gif ]

# #? na kursu smo stvorili kornjace ovako
# colors = ["red", "green", "orange", "yellow", "black", "blue"]
# y_position = [-180, -120, -60, 0, 60, 120, 180]

# for turtle_index in range(0,6):
#     tim = Turtle(shape="turtle")
#     tim.color(colors[turtle_index])
#     tim.penup()
#     tim.goto(x= -230, y =y_position[turtle_index])

# daje im razlicite brzine
# ko dodje na kraj dobije info da je pobedio

is_race_on = False

if aj_se_kladimo:
    is_race_on = True

while is_race_on:
    for kornjaca in sve_kornjace:
        if kornjaca.xcor() > 230:
            is_race_on = False
            pobednik = kornjaca.pencolor()
            if pobednik == aj_se_kladimo:
                print(f"Pobednik je {pobednik} kornjaca. POBEDILI STE.. AJMO NA RULET STO BI FILIP REKAO")
            else:
                print(f"Pobednik je {pobednik} kornjaca. Kaze se koraca.......")
        random_distance = random.randint(0,10)
        kornjaca.forward(random_distance)

screen = Screen()
screen.exitonclick()