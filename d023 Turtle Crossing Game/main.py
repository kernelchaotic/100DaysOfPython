import time
from turtle import Screen
from player_turtle import PlayerTurtle
from car_obstacle import CarOverhead
from scoreboard_class import Scoreboard

FINISH_LINE_Y = 280.0

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('bisque3')

turtle = PlayerTurtle()
scoreboard = Scoreboard()
cars = CarOverhead()

screen.listen()
screen.onkey(turtle.up, "Up")

loop_counter = 0
loop_car_increment = 10

game_running = True
while game_running:
    loop_counter += 1
    time.sleep(0.05)
    screen.update()
    cars.move()

    if loop_counter % loop_car_increment == 0:
        cars.new_car()

    if turtle.ycor() > FINISH_LINE_Y:
        cars.next_level()
        scoreboard.next_level()
        turtle.restart()
        loop_car_increment -= 2

    for car in cars.all_cars:
        if car.distance(turtle.pos()) < 18:
            scoreboard.game_over()
            game_running = False

screen.exitonclick()
