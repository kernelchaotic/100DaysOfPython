import os
import random
import time

logo = '''

  / _ \ _   _  ___  ___ ___ /__    \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/| | |  / _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| | |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \___,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
'''
print(logo)
print("Welcome to the Number Guessing Game!")



def the_game():
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Would you like to play on easy mode or hard mode?:  ").lower()
    number = random.randint(1, 100)
    game_finished = False
    print(f"For testing purposes, the number is {number}.")

    if difficulty == "easy" or difficulty == "easy mode" or difficulty == "e":
        attempts = 10
        while not game_finished:
            if attempts == 0:
                print(f"\nYou've run out of attempts. The number was {number}.")
                attempts -= 1
                try_again = input("Try again? Y/N:  ").lower()
                if try_again == "y" or try_again == "yes":
                    os.system('clear')
                    the_game()
                elif try_again == "n" or try_again == "no":
                    os.system('clear')
                    print("Goodbye!")
                    game_finished = True
                else:
                    print("I didn't understand that. Please reboot the program and try again.")
                    game_finished = True
            else:
                print(f"\nYou have {attempts} attempts remaining to guess the number.")
                player_guess = input("Make a guess:  ")
                attempts -= 1
                if not isinstance(player_guess, int):
                    print("\nI swear to god if this is another dividing by zero incident I will strangle you.\n")
                elif int(player_guess) == number:
                    print(f"You got it! The number was {number}.")
                    play_again = input("Do you want to play again? Y/N:  ").lower()
                    if play_again == "y" or play_again == "yes":
                        os.system('clear')
                        the_game()
                    elif play_again == "n" or play_again == "no":
                        os.system('clear')
                        print("Goodbye!")
                        game_finished = True
                    else:
                        print("I didn't get that. Terminating process.")
                        game_finished = True
                elif int(player_guess) > number:
                    print("Too high.")
                    print("Guess again.")
                elif int(player_guess) < number:
                    print("Too low.")
                    print("Guess again.")
                else:
                    print("Something broke. Tell D.")

    elif difficulty == "hard" or difficulty == "hard mode" or difficulty == "h":
        attempts = 5
        while not game_finished:
            if attempts == 0:
                print(f"\nYou've run out of attempts. The number was {number}.")
                attempts -= 1
                try_again = input("Try again? Y/N:  ").lower()
                if try_again == "y" or try_again == "yes":
                    os.system('clear')
                    the_game()
                elif try_again == "n" or try_again == "no":
                    os.system('clear')
                    print("Goodbye!")
                    game_finished = True
                else:
                    print("I didn't understand that. Please reboot the program and try again.")
                    game_finished = True
            else:
                print(f"\nYou have {attempts} attempts remaining to guess the number.")
                player_guess = input("Make a guess:  ")
                attempts -= 1
                if not isinstance(player_guess, int):
                    print("\nI swear to god if this is another dividing by zero incident I will strangle you.\n")
                elif int(player_guess) == number:
                    print(f"You got it! The number was {number}.")
                    play_again = input("Do you want to play again? Y/N:  ").lower()
                    if play_again == "y" or play_again == "yes":
                        os.system('clear')
                        the_game()
                    elif play_again == "n" or play_again == "no":
                        os.system('clear')
                        print("Goodbye!")
                        game_finished = True
                    else:
                        print("I didn't get that. Terminating process.")
                        game_finished = True
                elif int(player_guess) > number:
                    print("Too high.")
                    print("Guess again.")
                elif int(player_guess) < number:
                    print("Too low.")
                    print("Guess again.")
                else:
                    print("Something broke. Tell D.")

    elif difficulty == "both":
        os.system('clear')
        print("Well we don't always get what we want, do we sweetcheeks? Lower your expectations like the rest of us.")
        time.sleep(5)
        os.system('clear')
        the_game()
    else:
        print("I'm sorry, I didn't understand that. Please try again in a few seconds.")
        time.sleep(5)
        os.system('clear')
        the_game()


the_game()
