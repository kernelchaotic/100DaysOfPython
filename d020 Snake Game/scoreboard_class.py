from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 460)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write(
            arg=f'''GAME OVER
Score: {self.score}''',
            align=ALIGNMENT,
            font=("Courier", 40, 'normal')
        )
