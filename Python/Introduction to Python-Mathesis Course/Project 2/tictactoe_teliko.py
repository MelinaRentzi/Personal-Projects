# -*- coding: utf-8 -*-
# Άσκηση 16_1_template
# Κρίση εργασίας: (βαθμολόγηση όπως παρακάτω)
import random
import time

theBoard = [' '] * 10

marker = {'Παίκτης 1': 'X', 'Παίκτης 2': 'O', }

def display_board(board): # 4 μονάδες
    #εμφάνισε την κατάσταση της τρίλιζας
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


def choose_first(): # 2 μονάδες
    #κλήρωση για το ποιος θα παίξει πρώτος
    # επιστρέφει είτε 'Παίκτης 1' είτε 'Παίκτης 2'
    if random.randint(0, 1) == 0:
        return 'Παίκτης 1'
    else:
        return 'Παίκτης 2'
def display_score(score): # 2 μονάδες
    #Τυπώνει το τελικό σκορ
    print('ΤΕΛΙΚΟ ΣΚΟΡ')
    print('Παίκτης 1: ' + str(score['Παίκτης 1']))
    print('Παίκτης 2: ' + str(score['Παίκτης 2']))

def place_marker(board, marker, position): # 2 μονάδες
    #Τοποθετεί στη θέση position του board τον marker
    position = int(position)
    board[position]=marker

def win_check(theBoard,mark): # 4 μονάδες *
    #επιστρέφει True αν το σύμβολο mark έχει σχηματίσει τρίλιζα
    return ((theBoard[7] == mark and theBoard[8] == mark and theBoard[9] == mark) or # across the top
            (theBoard[4] == mark and theBoard[5] == mark and theBoard[6] == mark) or # across the middle
            (theBoard[1] == mark and theBoard[2] == mark and theBoard[3] == mark) or # across the bottom
            (theBoard[7] == mark and theBoard[4] == mark and theBoard[1] == mark) or # down the left side
            (theBoard[8] == mark and theBoard[5] == mark and theBoard[2] == mark) or # down the middle
            (theBoard[9] == mark and theBoard[6] == mark and theBoard[3] == mark) or # down the right side
            (theBoard[7] == mark and theBoard[5] == mark and theBoard[3] == mark) or # diagonal
            (theBoard[9] == mark and theBoard[5] == mark and theBoard[1] == mark)) # diagonal

def isSpaceFree(board,position):
    #επιστρέφει True αν το τετράγωνο που επιλέχθηκε είναι κενό (extra function)
    return board[position]==' '

def board_check(board): # 2 μονάδες
    #επιστρέφει False αν υπάρχουν ακόμη κενά τετράγωνα
    #και True στην αντίθετη περίπτωση.
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True
 
def player_choice(theBoard, turn): # 2 μονάδες *
    #Ο Παίκτης turn επιλέγει τετράγωνο
    #Επιστρέφει έναν ακέραιο στο διάστημα [1,9]
    #Εδώ θα γίνει και ο έλεγχος αν υπάρχει ήδη τιμή μέσα στο τετράγωνο
    position=' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(theBoard,int(position)):
        print('Διάλεξε τετράγωνο: (1-9)')
        position=input()
    return int(position)

def replay(): # 1 μονάδα
    # Ρωτάει τον χρήστη αν θέλει να ξαναπαίξει και επιστρέφει True αν ναι.
    print('Θέλετε να ξαναπαίξετε; (ναι ή όχι)')
    return input().lower().startswith('ν')

def next_player(turn): # 1 μονάδα
    #επιστρέφει τον επόμενο παίκτη που πρέπει να παίξει
    if turn == 'Παίκτης 1':
        print('Παίζει ο Παίκτης 2')
        return 'Παίκτης 2'
    else:
        print('Παίζει ο Παίκτης 1')
        return 'Παίκτης 1'

def main():
    score = {} # λεξικό με το σκορ των παικτών
    print('Αρχίζουμε!\nΓίνεται κλήρωση ', end = '')
    for t in range(10):
        print(".", flush='True', end=' ')
        time.sleep(0.2)
    print()
    # η μεταβλητή turn αναφέρεται στον παίκτη που παίζει
    turn = choose_first() 
    print("\nΟ " + turn + ' παίζει πρώτος.')
    # η μεταβλητή first αναφέρεται στον παίκτη που έπαιξε πρώτος
    first = turn 
    game_round = 1 # γύρος παιχνιδιού
    while True:
        # Καινούργιο παιχνίδι
        # Δημιουργία λίστας 10 στοιχείων βλέπε μάθημα 2 σελ.7 σημειώσεων
        theBoard = [' '] * 10 
        # Αφήστε το πρώτο στοιχείο δηλαδή το theBoard[0] κενό έτσι ώστε 
        # το index να αντιστοιχεί στην ονοματοδότηση των τετραγώνων 
        game_on = True  #ξεκινάει το παιχνίδι
        while game_on:
            display_board(theBoard) #Εμφάνισε την τρίλιζα
            # ο παίκτης turn επιλέγει θέση
            position = player_choice(theBoard, turn) 
            # τοποθετείται η επιλογή του
            place_marker(theBoard, marker[turn], position) 
            if win_check(theBoard, marker[turn]): # έλεγχος αν νίκησε
                display_board(theBoard)
                print('Νίκησε ο '+ turn)
                score[turn] = score.get(turn, 0) + 1
                game_on = False
            # έλεγχος αν γέμισε το ταμπλό χωρίς νικητή
            elif board_check(theBoard): 
                display_board(theBoard)
                print('Ισοπαλία!')
                game_on = False
            else: # αλλιώς συνεχίζουμε με την κίνηση του επόμενου παίκτη
                turn = next_player(turn)
        if not replay():
            ending = ''
            if game_round>1 : ending = 'υς'
            print("Μετά από {} γύρο{}".format(game_round, ending))
            display_score(score) # έξοδος ... τελικό σκορ
            break
        else :
            game_round += 1
            # στο επόμενο παιχνίδι ξεκινάει ο άλλος παίκτης
            turn = next_player(first) 
            first = turn
main()
