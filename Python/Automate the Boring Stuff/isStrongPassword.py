import re

uppersRegex = re.compile(r'[A-Z]')
lowersRegex = re.compile(r'[a-z]')
digitsRegex = re.compile(r'\d')

def strongPassword():
    while True:
        password = input('Please enter a password at least 8 characters long, \ncontaining at least 1 uppercase and 1 lowercase letter and at least 1 digit: ')
        if len(password) < 8:
            print('Your password needs to be at least 8 characters long.  Please try again!')
            continue
        elif not uppersRegex.search(password):
            print('Your password needs to contain at least one upper case character.  Please try again!')
            continue
        elif not lowersRegex.search(password):
            print('Your password needs to contain at least one lower case character.  Please try again!')
            continue
        elif not digitsRegex.search(password):
            print('Your password needs to contain at least one digit.  Please try again!')
            continue
        else:
            #we're happy with the value given.
            #we're ready to exit the loop.
            break
    print('Password accepted')
    return True

if __name__ == '__main__':
    print(strongPassword())