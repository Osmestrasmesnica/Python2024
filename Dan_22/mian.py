 #! PYTHON DAN 23

#Danas cu probati sam da napravim Pong Arcade Game...

#! 1. Create screen
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

def draw_dashed_line():
    line = Turtle()
    line.speed(0)
    line.color("white")
    line.penup()
    line.goto(0, 300)
    line.setheading(270)
    
    # Dash length and gap length
    dash_length = 15
    gap_length = 10
    
    for _ in range(50):
        line.pendown()
        line.forward(dash_length)
        line.penup()
        line.forward(gap_length)

    line.hideturtle()

screen = Screen()
screen.setup(width = 800, height = 580)
screen.bgcolor("black")
screen.title("Pong Arcade Game by WLQ")
screen.tracer(0)

# Draw the dashed line
draw_dashed_line()

#! 2./3. Create paddles 1 adn 2, and enable up down movement for 20px

paddle1 = Paddle(350)
paddle2 = Paddle(-350)

#! 4. Create ball and make it move
ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle1.up, "Up")
screen.onkeypress(paddle2.up, "w")
screen.onkeypress(paddle1.down, "Down")
screen.onkeypress(paddle2.down, "s")

game_is_on = True



while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #! 5. Detect collision with wall and bounce of it
    if ball.ycor() > 260 or ball.ycor() < -260:
         # should bounce
        ball.bounce_y()

    #! 6. Detect collision with paddle
    if ball.xcor() > 335 and ball.distance(paddle1) < 50 and ball.x_move > 0  or ball.xcor() < -335 and ball.distance(paddle2) < 50 and ball.x_move < 0:
        ball.bounce_x()
    #! 7. Detect if paddle miss a ball, and update score
    if ball.xcor() > 380:
        #update score, p2 +1
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        #reset ball position
        ball.reset()
    
    if ball.xcor() < -380:
        #update score, p2 +1
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        #reset ball position
        ball.reset()

    if scoreboard.l_score >= 5:
        game_is_on = False
        scoreboard.game_over("Left Player", f"{scoreboard.l_score} - {scoreboard.r_score}")
    elif scoreboard.r_score >= 5:
        game_is_on = False
        scoreboard.game_over("Right Player", f"{scoreboard.l_score} - {scoreboard.r_score}")

screen.exitonclick()