import random

answer = True
computer_score = 0
user_score = 0

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


def winner(user, computer):
    global computer_score, user_score
    if (user - computer) % 5 == 0:
        return "Dead heat \n"
    if (user - computer) % 5 >= 3:
        computer_score += 1
        return "Computer is winner \n"
    else:
        user_score += 1
        return "You are winner \n"


def input_winner(computer, user):
    print("you result: ", user,
          "computer result: ", computer)


def winner_congratulations(computer, user):
    if computer > user:
        print("\n ----- COMPUTER WIN! ------ \n")
        input_winner(computer, user)
    elif computer < user:
        print("\n ----- YOU WIN! ----- \n")
        input_winner(computer, user)
    else:
        print("\n ----- DEAD HEAT ----- \n")
        input_winner(computer_score, user_score)


def next_attempt(check_attempt):
    global answer, computer_score, user_score
    if check_attempt == "Y":
        answer = True
    elif check_attempt == "n":
        answer = False
        winner_congratulations(computer_score, user_score)
    else:
        answer = False
        print("Sorry, But you input invalid Char \n"
              "Farewell!!!\n")
        input_winner(computer_score, user_score)


while (answer):
    user_input = input("Input your figure: \n")
    print("You input: ", user_input)
    name_to_number(user_input)
    computer_input = random.randrange(0, 5, 1)
    print("Computer input: ", number_to_name(computer_input))
    print(winner(name_to_number(user_input), computer_input))
    check = input("Do you want to try again Y/n: \n")
    next_attempt(check)
