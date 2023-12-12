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

print("Welcome to treasure Island. Can You find the Treasure or will the Island claim another life?\n")
print("You will be given a situation and have to choose how to react. But choose carefully as wrong decisions may lead to death\n")

choice1 = input("You enter the Island and find yourself at a crossroad. Leading from it is a path to the left and a path to the right.\nWhich direction do you want to go? Left or Right?\n")
choice = choice1.lower()
if choice == "right":
    print("As you folow the right path you hear a click! When You turn around you notice a huge rock marble following you and the path leading into a literal dead end!\n!Game over!")
    quit()
elif choice == "left":
    print("You follow the path until the forrest clears and you find yourself standing on a pier.\nIn the distance You see a Boat slowly approaching.\n")
    choice2 = input("Do you want to wait or try to swim?")
    choice = choice2.lower()
    if choice == "swim":
        print("You enter the cold dark water and start swimming across, when you suddenly feel a hand grabbing your Leg and pull you deeper into the dark depths of the lake.\n!Game Over!\n")
        quit()
    elif choice == "wait":
        print("You patiently wait as the boat approches. You hop into the boat and are slowly taken across the lake to the island. When you look down into the depths of the lake you glimps arms reaching to the surface trying to grab what ever swims across.\nYou step of the boat and follow the trail which leads to a House.\n")
        choice3 = input("There are three doors. which do you want to enter the first second or third?\n")
        choice = choice3.lower()
        if choice == "third":
            print("You walk through the door and fall into a bottomless pitt.\n!Game Over!\n")
            quit()
        elif choice == "first":
            print("You walk into a room as the door closes behind you. suddenly the room fills with fire as you burn to death.\n!Game Over!\n")
            quit()
        elif choice == "second":
            print("You enter the house and follow the steps into the basement. Ther You find a Chest filled to the top with Gold Coins.\nCongratulation you found the Treasure.\n")
            quit()
