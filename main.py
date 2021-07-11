import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "a")
screen.onkey(paddle_l.go_down, "z")

game_start = True
while game_start:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < 50 and ball.xcor() > -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.center()
        score.point_l()
        score.update_score()

    if ball.xcor() < -380:
        ball.center()
        score.point_r()
        score.update_score()

    if score.score_r == 10 or score.score_l == 10:
        ball.stop()
        game_start = False

screen.clear()
turtle.bgcolor("black")
turtle.penup()
turtle.color("white")
turtle.hideturtle()
if score.score_r == 10:
    turtle.write("RIGHT WIN!!", True, align="center", font=("Arial", 50, "normal"))
else:
    turtle.write("Left WIN!!", True, align="center", font=("Arial", 50, "normal"))


screen.exitonclick()
