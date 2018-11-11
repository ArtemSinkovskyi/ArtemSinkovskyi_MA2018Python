import random

print(
    '''    *0 - "rock",
    *1 - "Spock",
    *2 - "paper",
    *3 - "lizard",
    *4 - "scissors"'''
)


def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Your input invalid name"


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Your input invalid number"


def winner(user):
    print("\nYou input: ", number_to_name(user))
    computer_input = random.randrange(0, 5, 1)
    print("Computer input: ", number_to_name(computer_input))
    if (user - computer_input) % 5 == 0:
        return "Dead heat"
    if (user - computer_input) % 5 >= 3:
        return "Computer is winner"
    else:
        return "You are winner"


print(winner(name_to_number("rock")))
print(winner(name_to_number("Spock")))
print(winner(name_to_number("paper")))
print(winner(name_to_number("lizard")))
print(winner(name_to_number("scissors")))
