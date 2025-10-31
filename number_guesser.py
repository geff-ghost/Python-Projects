import random

def validNumber(num: int):
    if num.isdigit():
        num = int(num)
        if num <= 0:
            print('Try a number greater than zero')
            return 0
        else:
            return num
    else:
        print('Invalid input')
        return 0
    
def guess(range_input, user_guess):
    value = random.randint(0, range_input)
    if user_guess > range_input:
        print('Out of range')
        return False
    elif user_guess == value:
        print('You guessed it correct ')
        return True
    elif user_guess < value:
        print('You guessed lower')
        return False
    else:
        print('You guessed higher')
        return False
        
    

play = input('Do you want to play: ')
if play != 'yes':
    quit()
else:
    top_range = input('Enter a range: ')
    range_input = validNumber(top_range)
    guesses = 0
    while True:
        choice = input('Make a guess: ')
        guesses += 1
        user_guess = validNumber(choice)
        correct = guess(range_input, user_guess)
        if correct:
            print(f'You got it in {guesses} guesses🥳🥳')
            break