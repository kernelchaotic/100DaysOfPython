
# at https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# the below code is a surefire way to get Reeborg to the goal each time

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() == False:
    if right_is_clear():
        turn_right()
    if wall_in_front():
        turn_left()
    else:
        move()
