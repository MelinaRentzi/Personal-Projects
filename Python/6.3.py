poem = '''

Εγώ μετράω τα ρέστα μου να βγάλω κι άλλο μήνα
ανοίγω και δε βλέπω ουρανό 
εσύ έχεις στο πιάτο σου ολόκληρη Αθήνα
ανοίγεις και χαζεύεις το κενό

'''
print(poem)

# H alfavhtikh lista lekswn

list_words= poem.split()
list_words.sort()
print(list_words)

#plithos leksewn

print("To plithos twn leksewn einai: {}".format(len(list_words)))

#plithos xarakthrwn
poem=poem.replace(" ","").replace('\n',"")
print("To plithos twn  grammatwn einai: {}".format(len(poem)))
