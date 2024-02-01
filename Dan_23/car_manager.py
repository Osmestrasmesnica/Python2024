from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


#! Ovo si ti aleksa zakomplikovao ali radi sve u sustini
# class CarManager(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.penup()
#         self.color(random.choice(COLORS)) 
#         self.shape('square')
#         self.shapesize(stretch_wid=1, stretch_len=2)
#         self.x_move = STARTING_MOVE_DISTANCE
#         self.y_coordinate = random.randint(-250,250)
#         self.goto(310, self.y_coordinate)
        
    
#     # napravi da se pomeraju ti kvadratici konstantnom brzinom, a kako se menja nivo tako se povecava brzina
#     def move(self):
#         new_x = self.xcor() - self.x_move
#         self.goto(new_x, self.ycor())

#     # napravi funkciju koja ce da povecavanja brzinu kretanja automobila kako nivoi idu
#     def increase_speed(self):
#         self.x_move += MOVE_INCREMENT
