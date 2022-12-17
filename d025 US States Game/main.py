import turtle
import tkinter
import pandas
from name_text_class import StateNames

screen = turtle.Screen()
names = StateNames()
screen.setup(width=725, height=491)
screen.bgpic('blank_states_img.gif')

states = pandas.read_csv("50_states.csv")


def popup(title, text):
    tkinter.messagebox.showinfo(title=title, message=text)


states_guessed = 0

game_running = True
while game_running:
    if states_guessed == 50:
        break
    else:
        pass

    answer_state = screen.textinput(title=f"{states_guessed}/50 States", prompt="Guess a state:").title()
    if answer_state in states.values:
        if answer_state not in names.names_added:
            names.names_added.append(answer_state)
            states_guessed += 1
            names.draw_state_name(answer_state)
        else:
            popup(title="Oops!", text=f"You have already guessed {answer_state}.")

    elif answer_state == "Peepee":
        popup(title="Peepee", text="Poopoo")
    elif answer_state == "69":
        popup(title="69", text="Nice.")
    elif answer_state == "420":
        popup(title="420", text="What's with you guys and the funny weed number?")
    elif answer_state == "69420":
        popup(title="69420", text="Now we're talking!")
    else:
        popup(title="Incorrect", text="That is not a state.")

popup(title="Congratulations!", text="You've successfully guessed all 50 states!")
popup(title="", text="...")
popup(title="", text="Go get a life, nerd.")

turtle.mainloop()
