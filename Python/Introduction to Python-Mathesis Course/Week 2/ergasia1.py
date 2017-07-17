# Test 1
# Μάντεψε έναν αριθμό 
 
import random #vivliothikh
 
find_me = random.randint(1,100)
print(find_me) #spoiler
 
tries = 0
points = 10
lower = 0
upper = 100
 
print("Έχω διαλέξει έναν αριθμό μεταξύ του {:d} και του {:d} \nδέχομαι μόνο ακέραιους αριθμούς ως έγκυρες λύσεις \nγια έξοδο γράψε 'exit' ".format(lower,upper))
 
while True :
    guess_number = input('Μπορείς να μαντέψεις τον αριθμό; ')
 
    if guess_number != 'exit' :
        try : guess_number = int(guess_number)
        except ValueError  : guess_number = -1
     
    if guess_number == 'exit' :
        if tries ==1 :
               print('Επέλεξες να τερματίσεις το παιχνίδι μετά από {:d} προσπάθεια'.format(tries))
        else :
               print('Επέλεξες να τερματίσεις το παιχνίδι μετά από {:d} προσπάθειες'.format(tries))
        break
 
    elif guess_number == find_me :
        if tries == 0 and points-tries>0:
            print ('Μπράβο!!! ο αριθμός είναι ο {:d}, το βρήκες σε {:d} προσπάθεια και οι πόντοι σου είναι {:d}'.format(find_me,tries+1,points-tries))
        if tries>0 and points-tries>0 :
            print ('Μπράβο!!! ο αριθμός είναι ο {:d}, το βρήκες σε {:d} προσπάθειες και οι πόντοι σου είναι {:d}'.format(find_me,tries+1,points-tries))
        else :
            print ('Μπράβο!!! ο αριθμός είναι ο {:d}, το βρήκες σε {:d} προσπάθειες και οι πόντοι σου είναι {:d}'.format(find_me,tries+1,0))         
        break
                   
    elif guess_number < 0 or guess_number > 100 :
            print('μη αποδεχτή είσοδος! ')
            tries +=1
            continue
         
    elif guess_number > find_me :
        if upper >= guess_number :
            upper = guess_number-1
 
        print(' Όχι, είναι μικρότερος!! \nο αριθμός που ψάχνεις, είναι μεταξύ των {:d} και {:d} '.format(lower,upper))
        tries +=1
        continue
    elif guess_number < find_me :
        if lower <= guess_number :
            lower = guess_number+1
        print(' Όχι, είναι μεγαλύτερος!! \nο αριθμός που ψάχνεις, είναι μεταξύ των {:d} και {:d} '.format(lower,upper))
        tries +=1
        continue
