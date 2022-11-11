from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        if self.ycor() < 275:
            self.goto(x=self.xcor(), y=self.ycor() + 20)
        else:
            pass

    def down(self):
        if self.ycor() > -275:
            self.goto(x=self.xcor(), y=self.ycor() - 20)
        else:
            pass


class ComputerPaddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.y_direction = 7

    def move(self):
        self.goto(x=self.xcor(), y=self.ycor() + self.y_direction)

    def flip(self):
        self.y_direction *= -1
