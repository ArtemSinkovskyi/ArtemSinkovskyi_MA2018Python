import random

elementsInGame = \
    ["rock", "Spock", "paper", "lizard", "scissors"]


def winner(user_option):
    computer_option = random.randint(0, 4)
    print("\nYour variant is: ", elementsInGame[user_option],
          "\nComputer variant is: ", elementsInGame[computer_option], )
    if user_option == computer_option:
        print("Dead heat")
    elif computer_option == 0 and (user_option == (3 or 4)) \
            or computer_option == 1 and (user_option == (4 or 0)) \
            or computer_option == 2 and (user_option == (0 or 1)) \
            or computer_option == 3 and (user_option == (1 or 2)) \
            or computer_option == 4 and (user_option == (2 or 3)):
        print("Computer is WINNER")
    else:
        print("You are WINNER")


for i in elementsInGame:
    winner(elementsInGame.index(i))
