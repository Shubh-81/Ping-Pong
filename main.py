from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Ping Pong")
screen.tracer(0)

lpaddle = Paddle((-350,0))
rpaddle = Paddle((350,0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(rpaddle.move_up,"Up")
screen.onkey(rpaddle.move_down,"Down")
screen.onkey(lpaddle.move_up,"w")
screen.onkey(lpaddle.move_down,"s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ybounce()
    
    if ball.distance(rpaddle) < 50 and ball.xcor() > 320:
        ball.xbounce()

    if ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.xbounce()

    if ball.xcor() > 380:
        scoreboard.l_score+=1
        scoreboard.update_scoreboard()
        ball.reset_position()
        ball.x_move+=2
        ball.y_move+=2
    
    if ball.xcor() < -380:
        scoreboard.r_score+=1
        scoreboard.update_scoreboard()
        ball.reset_position()
        ball.x_move+=2
        ball.y_move+=2


screen.exitonclick()