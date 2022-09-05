#Tic-Tac-Toe
import os

clear = lambda: os.system('cls')

# User Setup
names = ['','']
markers = ['X', 'O']

def user_setup():
    clear()
    print('Player 1 enter your name: ')
    names[0] = input()
    clear()
    print('Player 2 enter your name: ')
    names[1] = input()
    
    print(f"{names[0]} is {markers[0]}s. {names[1]} is {markers[1]}s")


# Game Setup
cells = [1, 2, 3, 4, 5, 6, 7, 8 , 9]
player_turn = 0
last_cell = ''
next_move = ''


# Display the Board
def show_board():
    clear()
    
    print('     |     |     ')
    print(f'  {cells[0]}  |  {cells[1]}  |  {cells[2]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {cells[3]}  |  {cells[4]}  |  {cells[5]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {cells[6]}  |  {cells[7]}  |  {cells[8]}  ')
    print('     |     |     ')


# Take Player Input
def input_check(selection):
    return cells[selection-1] is not 'X' and cells[selection-1] is not 'O'

def pick_cell():
    valid_input = False
    empty_cell = False

    while valid_input == False or empty_cell == False:
        valid_input = False
        empty_cell = False

        print(f'\n{names[player_turn]}, please enter a cell for your next move:')
        selection = -1

        while not valid_input and not empty_cell:
            user_input = int(input())
            if user_input > 0 and user_input < 10:
                selection = user_input
                valid_input = True
        
        empty_cell = input_check(selection)

        if valid_input and empty_cell:
            return selection
    
        print('\nInvalid selection.')


# Replace Cell
def replace_cell(cell):
    cells[cell-1] = markers[player_turn]


# Win Checking
def win_check(cells):
    if cells[0] == cells[1] == cells[2]:
        return True
    elif cells[3] == cells[4] == cells[5]:
        return True
    elif cells[6] == cells[7] == cells[8]:
        return True
    elif cells[0] == cells[3] == cells[6]:
        return True
    elif cells[1] == cells[4] == cells[7]:
        return True
    elif cells[2] == cells[5] == cells[8]:
        return True
    elif cells[0] == cells[4] == cells[8]:
        return True
    elif cells[2] == cells[4] == cells[6]:
        return True
    else:
        return False

# End Game
def end_game():
    print(f'\nCongrats, {names[player_turn]}! You are the winner!\n\n')


# Game Loop
user_setup()
win = False

while not win:
    show_board()
    replace_cell(pick_cell())
    win = win_check(cells)

    if win is True:
        show_board()
        end_game()

    if len(set(cells)) == 2:
        show_board()
        print('\n\nThis game is a draw!\n\n')
        break

    if player_turn == 0:
        player_turn = 1
    else:
        player_turn = 0

    


