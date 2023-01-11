
from tkinter import *
import random
import pandas as pd


# ------------------------ CONSTANTS -----------------------

LANGUAGE_FONT = ('Arial', 40, 'italic')
WORD_FONT = ('Arial', 60, 'bold')
BACKGROUND_COLOR = "#B1DDC6"

# ------------------------ CREATE VOCAB DATAFRAME -----------------------

# grab words from file
try:
    de_dict = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    de_dict = pd.read_csv('data/german_words.csv')
to_learn = de_dict.to_dict(orient='records')
current_card = {}


# ------------------------ FLIP CARD -----------------------

def next_card():
    global current_card
    current_card = random.choice(to_learn)
    flashcard.itemconfig(fc_image, image=fc_front)
    flashcard.itemconfig(fc_lang_label, text="Deutsch", fill='black')
    flashcard.itemconfig(fc_word_label, text=f"{current_card['German']}", fill='black')
    window.after(3000, func=flip_card)


def flip_card():
    flashcard.itemconfig(fc_image, image=fc_back)
    flashcard.itemconfig(fc_lang_label, text="English", fill='white')
    flashcard.itemconfig(fc_word_label, text=f"{current_card['English']}", fill='white')


# ------------------------ CHECK BUTTON FUNCTION -----------------------

# removes word from list of words to learn
def check_button_click():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()
    window.after(3000, func=flip_card)


# ------------------------ UI SETUP -----------------------

# window setup
window = Tk()
window.title("German / English Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

window.after(3000, func=flip_card)

# flashcard setup
flashcard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
fc_front = PhotoImage(file='./images/card_front.png')
fc_back = PhotoImage(file='./images/card_back.png')
fc_image = flashcard.create_image(400, 263, image=fc_front)
fc_lang_label = flashcard.create_text(400, 150, text="", font=LANGUAGE_FONT, fill='black')
fc_word_label = flashcard.create_text(400, 263, text="", font=WORD_FONT, fill='black')

flashcard.grid(column=0, row=0, columnspan=2)

# buttons setup
checkmark = PhotoImage(file='./images/right.png')
checkmark_button = Button(image=checkmark, highlightthickness=0, command=check_button_click)
checkmark_button.grid(column=0, row=1)

cross = PhotoImage(file='./images/wrong.png')
cross_button = Button(image=cross, highlightthickness=0, command=next_card)
cross_button.grid(column=1, row=1)

next_card()

window.mainloop()
