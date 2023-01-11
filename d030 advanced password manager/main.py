from tkinter import *
import random
import tkinter.messagebox
import password_character_bank as passcb
import json


# --------------------- POP-UP BOXES -------------------------------

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
    website = website_entry.get().title()
    email = email_entry.get()
    username = user_entry.get()
    if username == "":
        username = "No Username"
    password = password_entry.get()
    twofa = two_factor_auth_entry.get()

    # dict formatting for data.json file
    new_data = {
        website: {
            "email": email,
            "username": username,
            "password": password,
            "has 2FA?": twofa
        }
    }

    # check for needed fields and errors
    if password == "" or email == "" or website == "":
        popup(title="Crucial Field Blank", text='''Only 'Username' may be left blank.''')
    else:
        okay_cancel = tkinter.messagebox.askokcancel(title=f"{website}", message=f"Is this correct?\nWebsite: {website}\n"
                                                     f"Email: {email}\nUsername: {username}\nPassword: {password}")
        if okay_cancel:
            try:
                # reading old data
                with open("data.json", 'r') as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                # create new data.json
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # add data to existing json file
                with open("data.json", 'w'):
                    json.dump(new_data, data, indent=4)

            # clear entry fields
            entries_list = [website_entry, email_entry, user_entry, password_entry, two_factor_auth_entry]
            for entry in entries_list:
                entry.delete(0, 'end')

        else:
            popup(title="Please Review", text="Please review your inputs.")


# --------------------- SEARCH FUNCTIONALITY ---------------------------

def search_entries():
    website = website_entry.get().title()
    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
            search_results = data[website]
            popup(title=f"{website}",
                  text=f'''Email: {search_results['email']}
Username: {search_results['username']}
Password: {search_results['password']}
Has 2FA?: {search_results['has 2FA?'].upper()}''')

    except FileNotFoundError:
        popup(title="No Existing Data", text="No existing data available.")
    except KeyError:
        popup(title="No Entry Found", text="No entries from that website found.")


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

two_factor_auth_label = Label(text="Has 2FA? (Y/N): ", bg='white', highlightthickness=0)
two_factor_auth_label.grid(column=0, row=5)

# entry boxes
website_entry = Entry(width=25, bg='white', highlightthickness=0)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=40, bg='white', highlightthickness=0)
email_entry.grid(column=1, row=2, columnspan=2)

user_entry = Entry(width=40, bg='white', highlightthickness=0)
user_entry.grid(column=1, row=3, columnspan=2)

password_entry = Entry(width=25, bg='white', highlightthickness=0)
password_entry.grid(column=1, row=4)

two_factor_auth_entry = Entry(width=40, bg='white', highlightthickness=0)
two_factor_auth_entry.grid(column=1, row=5, columnspan=2)

# buttons
search_websites_button = Button(text="Search Entries", font=('Arial', 10), command=search_entries,
                                width=14, bg='white', highlightthickness=0)
search_websites_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate Password", font=('Arial', 10), command=generate_password,
                                  width=14, bg='white', highlightthickness=0)
generate_password_button.grid(column=2, row=4)

add_button = Button(text="Add", width=37, command=add_entry, bg='white', highlightthickness=0)
add_button.grid(column=1, row=6, columnspan=2)

# canvas setup with logo
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

window.mainloop()
