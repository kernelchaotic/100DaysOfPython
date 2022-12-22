from tkinter import *
import random
import tkinter.messagebox
import password_character_bank as passcb


# --------------------- POP-UP BOXES ------------------------------- #

def popup(title, text):
    tkinter.messagebox.showinfo(title=title, message=text)


# --------------------- PASSWORD GENERATOR -----------------------------

def generate_password():
    password = ""
    for character in range(5):
        letter = random.choice(passcb.letters)
        symbol = random.choice(passcb.symbols)
        integer = random.choice(passcb.numbers)
        password += letter + symbol + integer

    shuffling_password = list(password)
    random.shuffle(shuffling_password)
    strong_password = "".join(shuffling_password)
    password_entry.delete(0, 'end')
    password_entry.insert(0, strong_password)
    return strong_password


# ---------------------- SAVE PASSWORD ---------------------------------

def add_entry():
    website = website_entry.get()
    email = email_entry.get()
    username = user_entry.get()
    password = password_entry.get()
    if password == "" or email == "" or website == "":
        popup(title="Crucial Field Blank", text='''Only 'Username' may be left blank.''')
    else:
        okay_cancel = tkinter.messagebox.askokcancel(title=f"{website}", message=f"Is this correct?\nWebsite: {website}\n"
                                                     f"Email: {email}\nUsername: {username}\nPassword: {password}")
        if okay_cancel:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {username} | {password}\n")
        else:
            popup(title="Please Review", text="Please review your inputs.")


# ---------------------- UI WINDOW SETUP -------------------------------
# window setup
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg='white', highlightthickness=0)

# labels
website_label = Label(text="Website: ", bg='white', highlightthickness=0)
website_label.grid(column=0, row=1)

email_label = Label(text="Email: ", bg='white', highlightthickness=0)
email_label.grid(column=0, row=2)

username_label = Label(text="Username: ", bg='white', highlightthickness=0)
username_label.grid(column=0, row=3)

password_label = Label(text="Password: ", bg='white', highlightthickness=0)
password_label.grid(column=0, row=4)

# entry boxes
website_entry = Entry(width=40, bg='white', highlightthickness=0)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=40, bg='white', highlightthickness=0)
email_entry.grid(column=1, row=2, columnspan=2)

user_entry = Entry(width=40, bg='white', highlightthickness=0)
user_entry.grid(column=1, row=3, columnspan=2)

password_entry = Entry(width=24, bg='white', highlightthickness=0)
password_entry.grid(column=1, row=4)

# buttons
generate_password_button = Button(text="Generate Password", font=('Arial', 10), command=generate_password,
                                  width=14, bg='white', highlightthickness=0)
generate_password_button.grid(column=2, row=4)

add_button = Button(text="Add", width=37, command=add_entry, bg='white', highlightthickness=0)
add_button.grid(column=1, row=5, columnspan=2)

# canvas setup with logo
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

window.mainloop()
