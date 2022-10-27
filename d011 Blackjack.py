import random
import time
import os


logo = ("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")

player_hand = []
computer_hand = []
card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def serve_cards():
    for card in range(0, 2):
        player_hand.append(random.choice(card_deck))
    for card in range(0, 2):
        computer_hand.append(random.choice(card_deck))


def calculating_score():
    player_score = sum(player_hand)
    computer_score = sum(computer_hand)
    if player_score > 21:
        print("\nYou went over. You lose.")
    elif player_score < 21 < computer_score:
        print("\nOpponent went over. You win!")
    elif player_score < computer_score < 21:
        print("\nOpponent scored higher. You lose.")
    elif computer_score < player_score < 21:
        print("\nYou scored higher. You win!")
    elif computer_score == 21:
        print("\n Computer got Blackjack. You lose.")
    else:
        print("\nBlackjack! You win!")


game_start = input("Do you want to play a game of BlackJack? Y/N:  ").lower()
game_end = False

if game_start == "y" or game_start == "yes":
    while not game_end:
        os.system('clear')
        print(logo)
        serve_cards()
        p_score = sum(player_hand)
        c_score = sum(computer_hand)
        print("Your cards: " + str(player_hand) + ", current score: " + str(p_score))
        print("Computer's first card: " + str(computer_hand[0]))

        another_card = input("Pull another card? Y/N:  ").lower()
        if another_card == "y" or another_card == "yes":
            player_hand.append(random.choice(card_deck))
            computer_hand.append(random.choice(card_deck))
            p_score = sum(player_hand)
            c_score = sum(computer_hand)
            if 11 in player_hand and p_score > 21:
                p_score -= 10
            if 11 in computer_hand and c_score > 21:
                c_score -= 10
            print("Your final hand: " + str(player_hand) + ", final score: " + str(p_score))
            print("Computer's final hand: " + str(computer_hand) + ", final score: " + str(c_score))
        else:
            computer_pull = random.randint(0, 3)
            if computer_pull == 1:
                computer_hand.append(random.choice(card_deck))
                p_score = sum(player_hand)
                c_score = sum(computer_hand)
                if 11 in player_hand and p_score > 21:
                    p_score -= 10
                if 11 in computer_hand and c_score > 21:
                    c_score -= 10
                print("Your final hand: " + str(player_hand) + ", final score: " + str(p_score))
                print("Computer's final hand: " + str(computer_hand) + ", final score: " + str(c_score))
            else:
                print("Your final hand: " + str(player_hand) + ", final score: " + str(p_score))
                print("Computer's final hand: " + str(computer_hand) + ", final score: " + str(c_score))

        calculating_score()

        game_restart = input("Do you want to play again? Y/N:  ")
        if game_restart == "y" or game_start == "yes":
            os.system('clear')
            player_hand = []
            computer_hand = []
        elif game_restart == "n" or game_start == "no":
            os.system('clear')
            print("Goodbye!")
            game_end = True
        else:
            os.system('clear')
            print("Error 404")
            print("System Rebooting.")
            time.sleep(0.5)
            os.system('clear')
            print("Error 404")
            print("System Rebooting..")
            time.sleep(0.5)
            os.system('clear')
            print("Error 404")
            print("System Rebooting...")
            time.sleep(0.5)
            os.system('clear')
            print("Error 404")
            print("System Rebooting.")
            time.sleep(0.5)
            os.system('clear')
            print("Error 404")
            print("System Rebooting..")
            time.sleep(0.5)
            os.system('clear')
            print("Error 404")
            print("System Rebooting...")
            time.sleep(0.5)
            os.system('clear')
            print("Error 404")
            print("Restart complete.")
            player_hand = []
            computer_hand = []
            time.sleep(2)

else:
    print('''
    What the fuck did you just fucking say to me, you little bitch? I'll have you know I graduated top of my
    class in the Navy Seals, and I've been involved in numerous secret raids on Al-Qaeda, and I have over 300 
    confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are
    nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has 
    never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit 
    to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across 
    the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that 
    wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, 
    and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively 
    trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I 
    will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If 
    only you could have known what unholy retribution your little "clever" comment was about to bring down upon 
    you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the 
    price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.
    ''')
