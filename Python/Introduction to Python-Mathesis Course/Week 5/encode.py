encodings = [ 'utf-8', 'windows-1253']        
        
while True:
    f = input('όνομα αρχείου:')
    for e in encodings:
        try:
            fil =open(f, 'r', encoding = e, errors='strict')
            l = fil.read()
            fil.seek(0)
        except UnicodeDecodeError as e:
            print(e)
        except FileNotFoundError:
            print('Το αρχείο {} δεν βρέθηκε'.format(f))
        else :
            print(' To αρχείο {} έχει κωδικοποίηση {}'.format(f,e))
            break
