 #! PYTHON DAN 24
#! Turtle Crossing Road Game 

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, "Up")
screen.onkeypress(player.move, "w")

# #napravi praznu listu sa cars
# cars = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collisions with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
        
        # Sakrij kola ako predju ekran
        if car.xcor() < -310:
            car.hideturtle()
            car.clear()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.reset()
        car_manager.level_up()
        scoreboard.update_scoreboard()
        sleep(1)


screen.exitonclick()
    
    #! ovo si ga ti zakomplikovao Aleksa...ali radilo je (nije scoreboard radio samo lepo)
    # # Randomly generate a new car occasionally
    # if random.randint(1, 6) == 1:
    #     new_car = CarManager()
    #     cars.append(new_car)

    # # Move each car
    # for car in cars:
    #     car.move()

    # # Check the collision with car
    # for car in cars:
    #     if player.distance(car) < 30:
    #         game_is_on = False
    #         scoreboard.game_over()
    #         break # Exit the loop once the collision is detected
    
    # if not game_is_on:
    #     break
        
    # # Remove cars that have gone off-screen
    # car_manager.all_cars = [car for car in cars if car.xcor() > -310]
    
    # # Check if the frog managed to cross the road
    # if player.ycor() > 280:
    #     for car in cars:
    #         car.clear()
    #         car.hideturtle()
    #     cars = []  # Clear the cars list
    #     for car in cars:
    #         car.increase_speed()
    #     scoreboard.update_scoreboard()
    #     player.reset()

