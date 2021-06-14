import random
import os
os.system('color')
OKRED = '\33[31m'
CEND = '\033[0m'

a = "   ______ "
b = "   |"
c = "   |"
d = "   |"
e = "   |"
f = "   |"
g = "   |       "
h = " -----     "
aa = OKRED + "    | " + CEND
bb = OKRED + "    O " + CEND
cc1 = OKRED + "   /" + CEND
cc2 = OKRED + " \ " + CEND
dd = OKRED + "    | " + CEND
ee1 = OKRED + "   /" + CEND
ee2 = OKRED + " \ " + CEND



def print_wrong(choices):
    print(OKRED)
    print('Letter not guessed. You have only ' + str(choices) + ' left.')
    print(CEND)

def show_hang(choices):
    if choices == 7:
        hangman = (f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n{h}')
    elif choices == 6:
        hangman = (f'{a}\n{b}{aa}\n{c}\n{d}\n{e}\n{f}\n{g}\n{h}')
        print_wrong(choices)
    elif choices == 5:
        hangman = (f'{a}\n{b}{aa}\n{c}{bb}\n{d}\n{e}\n{f}\n{g}\n{h}')
        print_wrong(choices)
    elif choices == 4:
        hangman = (f'{a}\n{b}{aa}\n{c}{bb}\n{d}{cc1}\n{e}\n{f}\n{g}\n{h}')
        print_wrong(choices)
    elif choices == 3:
        hangman = (f'{a}\n{b}{aa}\n{c}{bb}\n{d}{cc1}{cc2}\n{e}\n{f}\n{g}\n{h}')
        print_wrong(choices)
    elif choices == 2:
        hangman = (f'{a}\n{b}{aa}\n{c}{bb}\n{d}{cc1}{cc2}\n{e}{dd}\n{f}\n{g}\n{h}')
        print_wrong(choices)
    elif choices == 1:
        hangman = (f'{a}\n{b}{aa}\n{c}{bb}\n{d}{cc1}{cc2}\n{e}{dd}\n{f}{ee1}\n{g}\n{h}')
        print_wrong(choices)
    else:
        hangman = (f'{a}\n{b}{aa}\n{c}{bb}\n{d}{cc1}{cc2}\n{e}{dd}\n{f}{ee1}{ee2}\n{g}\n{h}')
        print_wrong(choices)
    return hangman




def take_word():
    wordlist = []
    file = open("words.txt")
    for line in file:
        cat = line.rstrip()
        wordlist.append(cat)
    word = random.choice(wordlist)
    return word

def user_in():
    while True:
        x = input('Alegeti o litera: ')
        if x.isalpha() and len(x) == 1:
            x = x.lower()
        else:
            print(OKRED + 'Doar  o litera' + CEND)
            continue
        break
    return x