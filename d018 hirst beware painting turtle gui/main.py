from turtle import Turtle, Screen
import random
import colorgram

extracted_colors = colorgram.extract('beware.gif', 50)
color_list = []
for color in extracted_colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    add_to_list = (r, g, b)
    color_list.append(add_to_list)

mr_turtle = Turtle()
screen = Screen()
screen.colormode(255)

mr_turtle.speed(0)
mr_turtle.penup()
x = -250.00
y = -250.00

for value in range(10):
    mr_turtle.sety(y)
    mr_turtle.setx(x)
    for _ in range(10):
        mr_turtle.color(random.choice(color_list))
        mr_turtle.dot(20)
        mr_turtle.forward(50)
    y += 50


screen.exitonclick()
