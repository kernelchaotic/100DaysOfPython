
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number != len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        user_answer = input(f"\nQ{self.question_number + 1}. {question.text} True or False?:  ").title()
        self.check_answer(user_answer, question.answer)
        self.question_number += 1

    def check_answer(self, user_answer, question_answer):
        if user_answer == question_answer:
            self.score += 1
            print(f"That is correct! Current score: {self.score}/12")
        else:
            print(f"That is incorrect. The correct answer was {question_answer}.")


