import random



options =['rock', 'paper', 'scissors']
user_wins = 0
computer_wins = 0


def wins(user_choice, computer_choice):
    global user_wins
    global computer_wins

    if user_choice == computer_choice:
        print('You tied 🤝')
        computer_wins += 1
        user_wins += 1
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print('You win')
        user_wins += 1
    elif user_choice == 'paper' and computer_choice == 'rock':
        print('You win')
        user_wins += 1
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print('You win')
        user_wins += 1
    else:
        print('Computer won')
        computer_wins += 1
        
    return user_choice, user_wins, computer_wins

def choices(user_choice):
    if user_choice == 'q':
        return 'q', user_wins, computer_wins
        
    if user_choice not in options:
        return 'invalid', user_wins, computer_wins
    
    random_number = random.randint(0, 2)
    # rock=0, paper=1, scissors=2
    computer_choice = options[random_number]
    print(f'Computer picked {computer_choice}')
    
    return wins(user_choice, computer_choice)
    

while True:
    user_choice = input('Choose Rock, Paper, Scissors or Q to quit: ').lower()
    human_choice, user_win, computer_win = choices(user_choice)
    
    if human_choice == 'q':
        break
    elif human_choice == 'invalid':
        continue
    
print(f'You won: {user_win} times')
print(f'Computer won: {computer_win} times')
print('Byee👋....')