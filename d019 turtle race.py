
# known bug: sometimes multiple turtles can win if they pass the line at the same time, which is very rare
# please forgive the spaghetti, I have been trying to clean it up but each time I do it breaks
# Everywhere that needs a popup is marked with a todo statement
# I need it to be able to work on unix systems, as well as windows/mac
# It would be sick if it could work on Replit, but that'll be a replit limitation

import tkinter
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=425)
screen.bgcolor("bisque3")
user_bet = screen.textinput("Make Your Bet",
                            '''Which turtle are you betting on?
(Red, Orange, Yellow, Green, Blue, Purple)''')

is_race_on = False

colors = ["DarkRed", "DarkOrange2", "Goldenrod", "DarkGreen", "DarkBlue", "DarkOrchid4"]
race_ready_turtles = []
turtle_position_x = -237.5
turtle_position_y = -170
c_index = 0
for name in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[c_index])
    c_index += 1
    new_turtle.penup()
    new_turtle.setpos(x=turtle_position_x, y=turtle_position_y)
    turtle_position_y += 67.5
    race_ready_turtles.append(new_turtle)

finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(226.0, 180.0)
finish_line.pendown()
finish_line.goto(226.0, -180.0)

if user_bet:
    is_race_on = True

betting_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

if user_bet == "red":
    betting_turtle = "DarkRed"
elif user_bet == "orange":
    betting_turtle = "DarkOrange"
elif user_bet == "yellow":
    betting_turtle = "Goldenrod"
elif user_bet == "green":
    betting_turtle = "DarkGreen"
elif user_bet == "blue":
    betting_turtle = "DarkBlue"
elif user_bet == "purple":
    betting_turtle = "DarkOrchid4"

def popup(title, text):
    tkinter.messagebox.showinfo(title = title, message = text)

while is_race_on:
    if user_bet not in betting_colors:
        popup(title="Invalid Input", text="Input invalid. Please restart the program.")
        screen.clear()
        is_race_on = False

    for turtle in race_ready_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 222:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == "DarkRed":
                popup(title="Red Turtle wins", text="The red turtle has won the race!")
            elif winning_turtle == "DarkOrange2":
                popup(title="Orange Turtle wins", text="The orange turtle has won the race!")
            elif winning_turtle == "Goldenrod":
                popup(title="Yellow Turtle wins", text="The yellow turtle has won the race!")
            elif winning_turtle == "DarkGreen":
                popup(title="Green Turtle wins", text="The green turtle has won the race!")
            elif winning_turtle == "DarkBlue":
                popup(title="Blue Turtle wins", text="The blue turtle has won the race!")
            elif winning_turtle == "DarkOrchid4":
                popup(title="Purple Turtle wins", text="The purple turtle has won the race!")
            if winning_turtle == betting_turtle:
                popup(title="You win!", text="You win!")
            else:
                popup(title="You lost.", text="You lost.")


screen.exitonclick()
