# Εργασία 1
# Μάντεψε έναν αριθμό

import random

secretNumber = random.randint(1,100)
# print(secretNumber) #spoiler

tries = 0
points = 10
lower = 0
upper = 100

print("Έχω επιλέξει έναν αριθμό μεταξύ του {:d} και του {:d}. \nΔέχομαι μόνο ακέραιους αριθμούς. \nΓια έξοδο γράψε stop".format(lower,upper))

while True :
      guessNumber = input ("Ποιόν αριθμό έχω επιλέξει;  ")

      if guessNumber != 'stop':
          try : guessNumber = int(guessNumber)
          except ValueError: guessNumber = -1

      if guessNumber == 'stop':
          if tries ==1:
              print('Επέλεξες να τερματίσεις το παιχνίδι μετά από {:d} προσπάθεια.'.format(tries))
          else :
              print('Επέλεξες να τερματίσεις το παιχνίδι μετά από {:d} προσπάθειες.'.format(tries))
          break

      elif guessNumber == secretNumber :
          if tries ==0 and points-tries>0:
              print("Μπράβο! Ο αριθμός είναι ο {:d}, το βρήκες σε {:d} προσπάθεια και μάζεψες {:d} πόντους.".format(secretNumber,tries+1,points-tries))
          if tries > 0 and points-tries > 0:
              print ("Μπράβο! Ο αριθμός είναι ο {:d}, το βρήκες σε {:d} προσπάθειες και μάζεψες {:d} πόντους.".format(secretNumber,tries+1,points-tries))
          elif tries>0 and points-tries<0:
              print("Μπράβο! Ο αριθμός είναι ο {:d}, το βρήκες σε {:d} προσπάθειες και μάζεψες {:d} πόντους.".format(secretNumber,tries+1,0))
          break

      elif guessNumber<0 or guessNumber>100:
          print("Μη αποδεκτός αριθμός!")
          tries+=1
          continue

      elif guessNumber>secretNumber:
          if upper>=guessNumber:
              upper = guessNumber-1

          print("ΌΧΙ, είναι μικρότερος! \nΟ αριθμός που ψάχνεις είναι μεταξύ των {:d} και {:d}.".format(lower,upper))
          tries +=1
          continue

      elif guessNumber <secretNumber:
          if lower<=guessNumber:
              lower=guessNumber+1
          print("ΌΧΙ, είναι μεγαλύτερος! \nΟ αριθμός που ψάχνεις είναι μεταξύ των {:d} και {:d}.".format(lower,upper))
          tries+=1
          continue
      
