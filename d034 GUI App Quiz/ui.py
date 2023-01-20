from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
GREEN = '#90EE90'
RED = '#FFCCCB'
QUESTION_FONT = ('Arial', 17, 'italic')
SCORE_FONT = ('Arial', 11)


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR, highlightthickness=0)

        self.score_label = Label(text=f'Score: {self.quiz.score}', font=SCORE_FONT, fg='white',
                                 bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, background='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text=f'Question Text',
            font=QUESTION_FONT,
            width=290)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        true_img = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=true_img, background=THEME_COLOR,
                                  highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(column=0, row=2)
        false_img = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=false_img, background=THEME_COLOR,
                                   highlightthickness=0, command=self.false_clicked)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background='white')
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=f'{q_text}')
        if q_text == "You've completed the quiz!":
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_clicked(self):
        answer = self.quiz.check_answer('True')
        self.player_feedback(answer)

    def false_clicked(self):
        answer = self.quiz.check_answer('False')
        self.player_feedback(answer)

    def player_feedback(self, answer):
        if answer:
            self.canvas.config(background=GREEN)
            self.score_label.config(text=f'Score: {self.quiz.score}')
        else:
            self.canvas.config(background=RED)
        self.window.after(2000, func=self.get_next_question)
