 #! PYTHON DAN 24
#! Files, Directories and Paths

#! 1 - Napraviti HIGH SCORE u Snake game koju smo vec napravili
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Zmijica")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.onkey(snake.cheat, "c")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)

    snake.move()

    #! Detect collisions with food 
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

        #! Update high_score if current score is greater than previous high_score

    #! Detect collisions with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #! Detect collisions with tail
    for segments in snake.snake_body[1:]: # --> koristimo slicing da uprostimo kod, izbacimo glavu iz segmenta
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()