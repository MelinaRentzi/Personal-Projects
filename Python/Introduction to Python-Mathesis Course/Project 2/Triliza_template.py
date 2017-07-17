# -*- coding: utf-8 -*-
# Άσκηση 16_1_template
# Κρίση εργασίας: (βαθμολόγηση όπως παρακάτω)
import random
import time

marker = {'Παίκτης 1': 'X', 'Παίκτης 2': 'O', }

def display_board(board): # 4 μονάδες
    #εμφάνισε την κατάσταση της τρίλιζας
    pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης

def choose_first(): # 2 μονάδες
    #κλήρωση για το ποιος θα παίξει πρώτος
    # επιστρέφει είτε 'Παίκτης 1' είτε 'Παίκτης 2'
    pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης

def display_score(score): # 2 μονάδες
    #Τυπώνει το τελικό σκορ
    pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης

def place_marker(board, marker, position): # 2 μονάδες
    #Τοποθετεί στη θέση position του board τον marker
    pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης

def win_check(board,mark): # 4 μονάδες *
    #επιστρέφει True αν το σύμβολο mark έχει σχηματίσει τρίλιζα
    pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης

def board_check(board): # 2 μονάδες
    #επιστρέφει False αν υπάρχουν ακόμη κενά τετράγωνα
    #και True στην αντίθετη περίπτωση.
    pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης
 
def player_choice(board, turn): # 2 μονάδες *
    #Ο Παίκτης turn επιλέγει τετράγωνο
    #Επιστρέφει έναν ακέραιο στο διάστημα [1,9]
    #Εδώ θα γίνει και ο έλεγχος αν υπάρχει ήδη τιμή μέσα στο τετράγωνο
    pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης

def replay(): # 1 μονάδα
    # Ρωτάει τον χρήστη αν θέλει να ξαναπαίξει και επιστρέφει True αν ναι.
    pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης

def next_player(turn): # 1 μονάδα
    #επιστρέφει τον επόμενο παίκτη που πρέπει να παίξει
    pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης

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
            print("Μετά {} γύρο{}".format(game_round, ending))
            display_score(score) # έξοδος ... τελικό σκορ
            break
        else :
            game_round += 1
            # στο επόμενο παιχνίδι ξεκινάει ο άλλος παίκτης
            turn = next_player(first) 
            first = turn
main()
