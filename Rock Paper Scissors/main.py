import random


while True:
    data = ['Rock', "Paper", "Scissors"]
    computer = data[random.randint(0, 2)]
    me = input("1:Rock   2:Paper   3:Scissors  :  ")

    match me:
        case '1':
            me = 'Rock'
        case '2':
            me = 'Paper'
        case '3':
            me = 'Scissors'

    print('Computer: ' + computer + ' | Me: ' + me)

    if computer == "Rock" and me == "Scissors":
        print("Computer won")

    elif computer == "Scissors" and me == "Paper":
        print("Computer won")

    elif computer == "Paper"and me == "Rock":
        print("Computer won")

    elif me == "Rock" and computer == "Scissors":
        print("I won")

    elif me == "Scissors" and computer == "Paper":
        print("I won")

    elif me == "Paper" and computer == "Rock":
        print("I won")

    else:
        print("Scoreless")
