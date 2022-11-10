from turtle import Turtle, Screen
import random
from snake_class import Snake


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.goto(random.randint(-450, 450), random.randint(-450, 450))

    def respawn(self):
        self.goto(random.randint(-450, 450), random.randint(-450, 450))

