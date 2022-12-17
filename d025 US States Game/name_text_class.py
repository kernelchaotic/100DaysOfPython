from turtle import Turtle
import pandas

ALIGNMENT = 'center'
FONT = ("Arial", 10, 'normal')


class StateNames:
    def __init__(self):
        self.states_list = pandas.read_csv("50_states.csv")
        self.names_added = []
        self.states_text = []

    def draw_state_name(self, state_input):
        new_state_name = Turtle()
        new_state_name.hideturtle()
        new_state_name.penup()
        state_coordinates = (
            int(self.states_list[self.states_list.state == state_input].x),
            int(self.states_list[self.states_list.state == state_input].y)
                )
        new_state_name.goto(state_coordinates)
        new_state_name.write(arg=state_input, align=ALIGNMENT, font=FONT)
