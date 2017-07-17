# -*- coding: utf-8 -*-

import random
import time

theBoard = [' '] * 10

marker = {'Player 1': 'X', 'Player 2': 'O', }

def display_board(board):
    #Display the tic tac toe board
 print('7  |8  |9')
 print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
 print('   |   |')
 print('-----------')
 print('4  |5  |6')
 print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
 print('   |   |')
 print('-----------')
 print('1  |2  |3')
 print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
 print('   |   |')

def choose_first(): 
    #Randomly chooses which player goes first
    # Returns 'Player 1' or 'Player 2'
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def display_score(score): 
    #Prints the final score
    print('Player 1: ' + str(score['Player 1']))
    print('Player 2: ' + str(score['Player 2']))

def place_marker(board, marker, position):
    #Puts marker at the position of the board
        position = int(position)
        board[position]=marker
            
def win_check(theBoard,mark):
    #Returns True if the mark symbol has achieved a tictactoe
    return ((theBoard[7] == mark and theBoard[8] == mark and theBoard[9] == mark) or # across the top
            (theBoard[4] == mark and theBoard[5] == mark and theBoard[6] == mark) or # across the middle
            (theBoard[1] == mark and theBoard[2] == mark and theBoard[3] == mark) or # across the bottom
            (theBoard[7] == mark and theBoard[4] == mark and theBoard[1] == mark) or # down the left side
            (theBoard[8] == mark and theBoard[5] == mark and theBoard[2] == mark) or # down the middle
            (theBoard[9] == mark and theBoard[6] == mark and theBoard[3] == mark) or # down the right side
            (theBoard[7] == mark and theBoard[5] == mark and theBoard[3] == mark) or # diagonal
            (theBoard[9] == mark and theBoard[5] == mark and theBoard[1] == mark)) # diagonal

def isSpaceFree(board,position):
    # Returns true if the passed move is free on the passed board. (created that myself, not in the template)
    return board[position]==' '

def board_check(board):
    #Returns False if there are still empty squares at the board
    #and True otherwise
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True
 
def player_choice(theBoard, turn):
    #Player turn chooses a square
    #He inputs an integer between [1,9]
    #Here we need to check if there is already a marker in the specific square
    position=' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(theBoard,int(position)):
        print('Which square do you pick? (1-9)')
        position=input()
    return int(position)

def replay():
    #Asks the user if he wants to play again and returns True if yes
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def next_player(turn):
    #Returns the next Player that needs to play
    if turn == 'Player 1':
        print('Player 2 plays')
        return 'Player 2'
    else:
        print('Player 1 plays')
        return 'Player 1'

def main():
    score = {} # Dictionary with the players' scores
    print('We begin!\nRandomizing ', end = '')
    for t in range(10):
        print(".", flush='True', end=' ')
        time.sleep(0.2)
    print()
    # variable turn refers to the player that plays at the time
    turn = choose_first() 
    print("\nThe " + turn + ' plays first.')
    #variable first refers to the player that played first
    first = turn 
    game_round = 1 # game round
    while True:
        # New game
        #Creating a list with 10 elements
        theBoard = [' '] * 10
        #Let theBoard[0] be empty so that names and index are the same
        game_on = True  #The game starts
        while game_on:
            display_board(theBoard) #Display the tictactoe
            #Player turn chooses a position
            position = player_choice(theBoard, turn) 
            #His choice is placed in the board
            place_marker(theBoard, marker[turn], position) 
            if win_check(theBoard, marker[turn]): # Check if he won
                display_board(theBoard)
                print('The winner is '+ turn)
                score[turn] = score.get(turn, 0) + 1
                game_on = False
            #Check if the board is full without a winner
            elif board_check(theBoard): 
                display_board(theBoard)
                print('Draw!')
                game_on = False
            else: # Else we continue with the next player move
                turn = next_player(turn)
        if not replay():
            ending = ''
            if game_round>1 : ending = 's'
            print("After {} round{}".format(game_round, ending))
            display_score(score) # exit ... final score
            break
        else :
            game_round += 1
            #at the next game the other player starts first
            turn = next_player(first) 
            first = turn
main()
