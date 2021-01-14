import projectgame
# import the random module
import random

print('Starting the Rock Paper Scissors game!')
player_name = input('Please enter your name: ')

print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
player_hand = int(input('Please enter a number (0-2): '))

if projectgame.validate(player_hand):
    # Assign a random number between 0 and 2 to computer_hand using randint
    computer_hand = random.randint(0,2)
    
    projectgame.print_hand(player_hand, player_name)
    projectgame.print_hand(computer_hand, 'Computer')

    result = projectgame.judge(player_hand, computer_hand)
    print('Result: ' + result)
else:
    print('Please enter a valid number')
