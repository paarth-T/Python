import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)

def game() :

    player = input("rock, paper or scissors ? :- ")
    print("Computer : " + computer)

    if player == computer :
        print("Tie !")
    elif player == "rock" :
        if computer == "paper":
            print("You loose !")
        elif computer == "scissors":
            print("You WIN !!!")
    elif player == "paper" :
        if computer == "scissors":
            print("You loose !")
        elif computer == "rock":
            print("You WIN !!!")
    elif player == "scissors" :
        if computer == "rock":
            print("You loose !")
        elif computer == "papper":
            print("You WIN !!!")
    else : print("Invalid input.")

print(computer)
rep = input("Lets start? >>>")

if rep == "yes":
    while rep == "yes":
        game()
        rep = input("Try again : ")
elif rep == "no":
    print(">>> STOP <<<")




