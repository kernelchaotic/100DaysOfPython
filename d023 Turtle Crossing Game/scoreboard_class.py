from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.current_level = 1
        self.goto(-220, 260)
        self.write(f"Level: {self.current_level}", align='center', font=FONT)

    def next_level(self):
        self.clear()
        self.current_level += 1
        self.write(f"Level: {self.current_level}", align='center', font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)
