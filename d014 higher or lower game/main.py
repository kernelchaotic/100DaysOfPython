import random
import os
from gamedata import logo
from gamedata import data
from gamedata import vs

# print logo
# while loop nested in a game function
# random number generator to pull celebs from gamedata.py
# keep track of correct answers
# clear terminal between comparisons

running = True
######### change above value to true when ready

print(logo)


def higher_or_lower():
    """The shell holding the entire Higher or Lower game from start to finish."""
    player_score = 0
    global running

    while running:
        celeb1 = random.randint(0, 49)
        celeb2 = random.randint(0, 49)
        if celeb2 == celeb1:
            celeb2 = random.randint(0, 49)
        celeb1_name = data[celeb1]['name']
        celeb2_name = data[celeb2]['name']

        if data[celeb1]['follower_count'] > data[celeb2]['follower_count']:
            higher = celeb1_name
        else:
            higher = celeb2_name

        print(f"Compare A: {data[celeb1]['name']}, a(n) {data[celeb1]['description']}, from {data[celeb1]['country']}.")
        print(vs)
        print(f"Against B: {data[celeb2]['name']}, a(n) {data[celeb2]['description']}, from {data[celeb2]['country']}.")

        def celeb_choice():
            """The function to change the A/B input into the correct celebrity variable."""
            chosen_celeb = input("Who do you think has more followers? Type 'A' or 'B':  ").lower()
            if chosen_celeb == 'a':
                chosen_celeb = celeb1_name
                return chosen_celeb
            elif chosen_celeb == 'b':
                chosen_celeb = celeb2_name
                return chosen_celeb
            else:
                print("\nInvalid input.\n")
                celeb_choice()

        if celeb_choice() == higher:
            player_score += 1
            os.system('clear')
            print(logo)
            print(f"That's right! Your current score is {player_score}.")
        else:
            os.system('clear')
            print(f"That is incorrect. The correct answer was {higher}.")
            print("Please restart the program to try again.")
            running = False


while running:
    higher_or_lower()
