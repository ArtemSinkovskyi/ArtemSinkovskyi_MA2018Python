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


user_input = input("Input your figure: \n")
print("You input: ", user_input)
name_to_number(user_input)
computer_input = random.randrange(0, 5, 1)
print("Computer input: ", number_to_name(computer_input))


def winner(user, computer):
    if (user - computer) % 5 == 0:
        return "Dead heat \n"
    if (user - computer) % 5 >= 3:
        return "Computer is winner \n"
    else:
        return "You are winner \n"


print(winner(name_to_number(user_input), computer_input))
