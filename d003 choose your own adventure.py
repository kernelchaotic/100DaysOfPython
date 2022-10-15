
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Quest to Treasure Island!")
print("Your mission is to find the treasure.")
cross_road = input("You are dropped off at a crossroad. Which path will you take? \"left\" or \"right\"\n")
if cross_road == "left":
    print("Along the left path is a gentle beach clearing. You spot a dock off in the distance.")
    dock = input("You can see the island. Do you take your chances and swim, or wait for a boat? \"swim\" or \"wait\"\n")
    if dock == "wait":
        print("A boat with no captain eerily approaches and takes you safely to the island. There is a lone house.")
        door = input("Which do you take? \"red,\" \"yellow,\" or \"blue\"?\n")
        if door == "red":
            print("You slowly open the red door, only to feel an immense heat surround you as you are immolated.")
            print("Try again?")
        elif door == "yellow":
            print("You open the yellow door. It creaks on its hinges, the room before you smelling strongly of musk.")
            print("It must have been decades since someone last entered. You struggle to see in the darkness.")
            print("A table and sofa stair back at you. Upon closer inspection, the sofa is actually just draped cloth.")
            print("You remove the cloth, and beneath it lies an unlocked chest. The lid all but falls off upon opening.")
            print("You've found the treasure.")
        else:
            print("The blue door gives way to what seems to be nothing. As you step inside, you realize that must")
            print("have applied to the floor as well. You drop down a long pit to your death.")
            print("Try again?")
    else:
        print("The current churns. Beneath you, a black abyss awaits. Beckoning... Your limbs begin to fail in the cold.")
        print("The last thing you see is a kaleidoscope of radiant light and the maw of something colossal closing around you.")
        print("Try again?")
else:
    print("Along the left path is a thick forest. In your clumsiness, you trip over a felled branch.")
    print("A hungry bear hears your struggle and attacks. Try again?")