import hgm_functions as fl
import os
os.system('color')
OKRED = '\33[31m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
CEND = '\033[0m'

generated_word = fl.take_word()
list_word = list(generated_word)

hidden_list = []
guess_list = []
right_guess_list = []
choices = 7

guess_list.append(list_word[0])
if list_word[-1] != list_word[0]:
    guess_list.append(list_word[-1])

hidden_list.append(list_word[0])
right_guess_list.append(list_word[0])
for i in range(len(list_word) - 2):
    if list_word[i+1] == list_word[0]:
        hidden_list.append(list_word[0])
        right_guess_list.append(list_word[0])
    elif list_word[i+1] == list_word[-1]:
        hidden_list.append(list_word[-1])
        right_guess_list.append(list_word[-1])
    else:
        hidden_list.append('_')
hidden_list.append(list_word[-1])
right_guess_list.append(list_word[-1])
print(OKBLUE)
print(hidden_list)
print(CEND)

while True:
    print('Used already: ' + str(list(guess_list)))
    guess = fl.user_in()
    for i in range(len(list_word) - 1):
        if list_word[i] == guess and guess not in guess_list:
            hidden_list.pop(i)
            hidden_list.insert(i, guess)
            right_guess_list.append(guess)
    if guess not in list_word:
        choices = choices - 1
        print(fl.show_hang(choices))
    elif guess in guess_list:
        print(OKRED)
        print('Letter already guessed. You have only ' + str(choices) + ' left.')
        print(CEND)
        print('Used already: ' + str(list(guess_list)))
    if guess not in guess_list:
        guess_list.append(guess)

    if len(right_guess_list) == len(list_word):
        print(OKGREEN + 'Congratulation, you guessed the word:' + CEND)
        print(OKGREEN + generated_word + CEND)
        break
    if choices == 0:
        print(OKRED + 'You were hanged.'+ CEND)
        print('Word = ' + generated_word)
        break

    print(OKBLUE)
    print(hidden_list)
    print(CEND)