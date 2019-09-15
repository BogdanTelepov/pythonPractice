import random
guessing_number = None
computer_guess_number = random.randint(1,10)

while True:
    guessing_number = int(input('Guess a number between 1 to 10: '))

    if guessing_number < computer_guess_number:
        print('Too low, try again!')
    elif guessing_number > computer_guess_number:
        print('Too high, try again!')
    elif guessing_number == computer_guess_number:
        print('You win!')
        play_again = input('Do you want to play again? (y/n) ')
        if play_again == 'y':
            computer_guess_number = random.randint(1,10)
            guessing_number = None
        else:
            print('Thank you for playing')
            break
