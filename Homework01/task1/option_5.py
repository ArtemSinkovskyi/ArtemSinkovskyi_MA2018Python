import random

dictionaryOfKeyElementsInGame = \
    ["rock", "Spock", "paper", "lizard", "scissors"]


def winner(user_option):
    computer_option = random.randint(0, 4)
    if user_option == computer_option:
        print("\nYour variant is: ", dictionaryOfKeyElementsInGame[user_option], \
              "\nComputer variant is: ", dictionaryOfKeyElementsInGame[computer_option], \
              "\nDead heat")
    elif computer_option == 0 and (user_option == 3 or user_option == 4) \
            or computer_option == 1 and (user_option == 4 or user_option == 0) \
            or computer_option == 2 and (user_option == 0 or user_option == 1) \
            or computer_option == 3 and (user_option == 1 or user_option == 2) \
            or computer_option == 4 and (user_option == 2 or user_option == 3):
        print("\nYour variant is: ", dictionaryOfKeyElementsInGame[user_option], \
              "\nComputer variant is: ", dictionaryOfKeyElementsInGame[computer_option], \
              "\nComputer is WINNER")
    else:
        print("\nYour variant is: ", dictionaryOfKeyElementsInGame[user_option], \
              "\nComputer variant is: ", dictionaryOfKeyElementsInGame[computer_option], \
              "\nYou are WINNER")


for i in dictionaryOfKeyElementsInGame:
    winner(dictionaryOfKeyElementsInGame.index(i))
