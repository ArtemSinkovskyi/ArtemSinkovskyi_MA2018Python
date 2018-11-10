import random

print(
    '''    *0 - "rock",
    *1 - "Spock",
    *2 - "paper",
    *3 - "lizard",
    *4 - "scissors"'''
)

dictionaryOfKeyElementsInGame = \
    ["rock", "Spock", "paper", "lizard", "scissors"]

user_input = input("Input your figure: \n")

user_input_number = dictionaryOfKeyElementsInGame.index(user_input)
computer_input = random.randint(0, 4)

print("Your variant is: ", user_input)
print("Computer variant is: ", dictionaryOfKeyElementsInGame[computer_input])


def winner(user_option, computer_option):
    if user_option == computer_option:
        return "Dead heat"
    elif computer_option == 0 and (user_option == 3 or user_option == 4) \
            or computer_option == 1 and (user_option == 4 or user_option == 0)\
            or computer_option == 2 and (user_option == 0 or user_option == 1)\
            or computer_option == 3 and (user_option == 1 or user_option == 2)\
            or computer_option == 4 and (user_option == 2 or user_option == 3):
        return "Computer is WINNER"
    else:
        return "You are WINNER"


print(winner(user_input_number, computer_input))
