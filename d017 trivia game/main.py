from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for dictionary in question_data:
    text = dictionary["text"]
    answer = dictionary["answer"]
    question_bank.append(Question(text, answer))

quiz_brain = QuizBrain(question_bank)

print("Welcome to Trivia! Ahead of you awaits a quiz to test your knowledge."
      "Every question will have a True or False answer, which must be fully typed out.")
ready_to_play = input("Are you ready to play? Y/N:  ").lower()

if ready_to_play == "y" or ready_to_play == "yes":
    while quiz_brain.still_has_questions():
        quiz_brain.next_question()

    print(f"\nYour final score is {quiz_brain.score}/{len(question_bank)}!")
    if quiz_brain.score < (len(question_bank) / 2):
        print("Trivia games might not be for you.")
    elif quiz_brain.score < (float(len(question_bank) * 0.9)):
        print("That's pretty good! I'd celebrate having more than half.")
    else:
        print("Spot on! You make a fantastic trivia player.\n")

elif ready_to_play == "n" or ready_to_play == "no":
    print("Why are you even here? Begone thot.")

else:
    print("Error 404: Input not found.\n"
          "System shutting down.")
