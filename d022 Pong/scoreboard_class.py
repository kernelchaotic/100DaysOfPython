from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.player_score = 0
        self.computer_score = 0
        self.goto(0, 150)
        self.write(f"{self.player_score}   {self.computer_score}",
                   align='center',
                   font=("Courier", 80, 'bold'))

    def player_point(self):
        self.player_score += 1

    def computer_point(self):
        self.computer_score += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 150)
        self.write(f"{self.player_score}   {self.computer_score}",
                   align='center',
                   font=("Courier", 80, 'bold'))


class Divisor(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pensize(width=5)
        self.penup()
        self.goto(0, 300)
        self.right(90)
        for value in range(20):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20)
