from turtle import Screen
from paddle_classes import Paddle, ComputerPaddle
from pong_ball_class import PongBall
from scoreboard_class import Scoreboard, Divisor
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)


player_paddle = Paddle((-450.0, 0.0))
computer_paddle = ComputerPaddle((450.0, 0.0))
ball = PongBall()
divisor = Divisor()
scoreboard = Scoreboard()


screen.onkey(player_paddle.up, "Up")
screen.onkey(player_paddle.down, "Down")


screen.update()
time.sleep(3)

game_on = True
while game_on:
    screen.update()
    ball.move()
    computer_paddle.move()
    time.sleep(0.01)

    if computer_paddle.ycor() < -275 or computer_paddle.ycor() > 275:
        computer_paddle.flip()

    if ball.distance(player_paddle) < 50 and ball.xcor() < -440 or ball.distance(computer_paddle) < 50 and ball.xcor() > 440:
        ball.paddle_bounce()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_bounce()

    if ball.xcor() < -500:
        scoreboard.computer_point()
        time.sleep(1)
        ball.recenter()
        scoreboard.update_scoreboard()
        screen.update()
        time.sleep(1)

    if ball.xcor() > 500:
        scoreboard.player_point()
        time.sleep(1)
        ball.recenter()
        scoreboard.update_scoreboard()
        screen.update()
        time.sleep(1)

screen.exitonclick()
