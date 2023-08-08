import random

print('This number is between 1 and 9')
while True:
    print('---------------')
    print('The game begins')
    computer = random.randint(1,9)
    chance = 0
    while True:
        guess = int(input('Guess for random number: '))
        chance += 1
        if guess > computer:
            if guess-computer >= 3:
                if chance == 3:
                    print('Game over')
                    break
                else:
                    print('Too High')
            else:
                if chance == 3:
                    print('Game over')
                    break
                else:
                    print('High')

        elif guess < computer:
            if computer-guess >= 3:
                if chance == 3:
                    print('Game over')
                    break
                else:
                    print('Too Low')
            else:
                if chance == 3:
                    print('Game over')
                    break
                else:
                    print('Low')
        else:
            if chance == 3:
                print('Game over')
                break
            else:
                print('Exactly right')
                break
        if chance == 3:
                print('Game over')
                break