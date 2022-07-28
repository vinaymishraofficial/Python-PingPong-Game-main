from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
ball=Ball()
scoreboard=Scoreboard()

screen.setup(width=800,height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)


l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))


screen.listen()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")



is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
 #to bounce the ball

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #DETECT COLLISION WITH THE PADDLE
    if ball.distance(r_paddle)<50 and ball.xcor()>300 or ball.distance(l_paddle)<50 and ball.xcor()<-300:
        ball.bounce_x()
    
    #Detect R paddle missing
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    #DETECT L PADDLE MISSING
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()