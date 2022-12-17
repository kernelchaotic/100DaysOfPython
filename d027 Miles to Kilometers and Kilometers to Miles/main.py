from tkinter import *

# this code uses a set of functions that changes a global variable "unit_to_unit" so another function works properly
# these functions are on lines 27 and 33

# window
window = Tk()
window.title("Units Converter")
window.minsize(width=600, height=400)
window.config(padx=20, pady=20)


# label
program_label = Label(text="Miles to Kilometers", font=("Arial", 20))
program_label.grid(column=1, row=0)


# entry
units_input = Entry()
units_input.grid(column=0, row=1)


# button functions
unit_to_unit = "mtk"


def mtk_button_clicked():
    global unit_to_unit
    program_label.config(text="Miles to Kilometers")
    unit_to_unit = "mtk"


def ktm_button_clicked():
    global unit_to_unit
    program_label.config(text="Kilometers to Miles")
    unit_to_unit = "ktm"


def convert():
    global unit_to_unit
    input_value = units_input.get()
    if unit_to_unit == "mtk":
        converted_kilometers = int(input_value) * 1.61
        window_conversion_text = Label(
            text=f"{input_value} miles is equal to {round(converted_kilometers, 1)} kilometers.",
            font=("Arial", 12))
        window_conversion_text.grid(column=1, row=2)
    elif unit_to_unit == "ktm":
        converted_miles = int(input_value) * 0.62
        window_conversion_text = Label(
            text=f"{input_value} kilometers is equal to {round(converted_miles, 1)} miles.",
            font=("Arial", 12))
        window_conversion_text.grid(column=1, row=2)


# buttons
miles_to_kilometers = Button(text="Miles to Kilometers", command=mtk_button_clicked)
kilometers_to_miles = Button(text="Kilometers to Miles", command=ktm_button_clicked)
convert_button = Button(text="Convert", command=convert)

miles_to_kilometers.grid(column=0, row=3)
kilometers_to_miles.grid(column=1, row=3)
convert_button.grid(column=1, row=1)

window.mainloop()
