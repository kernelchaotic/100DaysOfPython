import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2.5
MOVE_INCREMENT = 2.5
STARTING_X = 320


class CarOverhead:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        new_car = Turtle('square')
        new_car.color(random.choice(COLORS))
        new_car.penup()
        random_y = random.randint(-250, 250)
        new_car.goto(STARTING_X, random_y)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.seth(180)
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def next_level(self):
        self.car_speed += MOVE_INCREMENT

