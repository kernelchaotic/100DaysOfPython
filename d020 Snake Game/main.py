from turtle import Screen
from snake_class import Snake
from food_class import Food
from scoreboard_class import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0, 0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

snake_running = True
while snake_running:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # food collision
    if snake.head.distance(food) < 20:
        food.respawn()
        snake.extend_snake()
        scoreboard.add_score()

    # snake tail collision

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            snake_running = False

    # wall collision
    if 480 < snake.head.xcor() or snake.head.xcor() < -480 or 480 < snake.head.ycor() or snake.head.ycor() < -480:
        snake_running = False

scoreboard.game_over()


screen.exitonclick()
