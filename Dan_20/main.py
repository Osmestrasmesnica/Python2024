 #! PYTHON DAN 20
#! Screen setup, Animation, Snake segments, OOP, Keypress
from turtle import Turtle, Screen 
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#! Create Snake Body
# napraviti 3 spojena turtle objekta 
# svi turtle objekti treba da su 20x20px beli kvadrati
x = 0
y = 0
snake_body = []

# pravi telo od snake
for i in range(3):
    body_part = Turtle()
    body_part.shape("square")
    body_part.resizemode("user")
    body_part.shapesize(stretch_wid= 20/20 , stretch_len= 20/20) # ovo nisam bas skontao ali imas na ChatGPT objasnjenje sto je ovo ovako, ima veze sa turtle default size koji je 20 units
    body_part.penup()
    body_part.color('red')
    body_part.goto(x,y)
    body_part.speed(0)
    x -= 20
    snake_body.append(body_part)

#! Make Snake Move and make tail follow head position
# koristimo tracer() da napravimo animaciju i to radimo gore kod screen.tracer(0) i ne updatuje se slika dok se ne ne unesemo screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for segment_number in range(len(snake_body)-1, 0, -1): # START, STOP, STEP.. ako hocemo range 123, onda je start 1, stop 3, step 1, a ako hocemo 321 onda je start 3, stop 1, segment-1, ali zato sto prolazimo kroz listu, a ona pocinje sa 0, a zavrsava se sa n-1 onda krecemo od 2 a zavrsavamo na 0
        new_x = snake_body[segment_number-1].xcor() # pozivija x ose pretposlednjeg segmenta
        new_y = snake_body[segment_number-1].ycor() # pozivija y ose pretposlednjeg segmenta
        snake_body[segment_number].goto(new_x, new_y)
    snake_body[0].forward(20)

#! Make 3 class -> Snake, Food, Scoreboard - OOP PROGRAMMING
    
#! Control Snake with keyboard press




screen.exitonclick()