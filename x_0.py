from random import choice

user_mark = 'X'
comp_mark = 'O'

a1 = '1'
a2 = '2'
a3 = '3'
b1 = '4'
b2 = '5'
b3 = '6'
c1 = '7'
c2 = '8'
c3 = '9'

POI_0 = [5]             # prima alegere
POI_1 = [1, 3, 7, 9]    # a doua alegere
POI_2 = [2, 4, 6, 8]    # ultima alegere
POI = [POI_0, POI_1, POI_2]
# at_table = [0 , 1 , 2,  3 , 4,  5,  6,  7,  8 ]
play_table = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
num_played = []  # Lista cu numere folosite

print('Apasati \'q\' pentru exit')


def print_table():
    print(f'{play_table[0:3]}\n{play_table[3:6]}\n{play_table[6:9]}')


def user_input(num_played):
    while True:
        try:
            user_in = input('Your choose: ')
            user_in = int(user_in)
            if user_in == 0 or user_in > 9:
                print('Alegeti doar intre 1 si 9')
                continue
            print(f"ai ales numarul {user_in}")
            choose = user_in - 1
            if choose in num_played:
                print('Acest numar a fost jucat. Alegeti altul.')
                continue
            else:
                num_played.append(choose)
            break
        except ValueError:
            if user_in == 'q':
                exit()
            print('Introduceti doar cifre')
    return choose


def update_POI(POI, user_val):
    for item in POI:
        for i, v in enumerate(item):
            if user_val + 1 == v:
                item.pop(i)
    return POI


def who_win(play_table):
    a = play_table[:3]
    b = play_table[3:6]
    c = play_table[6:]
    d = play_table[0], play_table[3], play_table[6]  # [a1, b1, c1]
    e = play_table[1], play_table[4], play_table[7]  # [a2, b2, c2]
    f = play_table[2], play_table[5], play_table[8]  # [a3, b3, c3]
    g = play_table[0], play_table[4], play_table[8]  # [a1, b2, c3]
    h = play_table[2], play_table[4], play_table[6]  # [a3, b2, c1]
    tot = [a, b, c, d, e, f, g, h]
    for item in tot:
        if item[0] == item[1] == item[2]:
            print('WINNER')
            print_table()
            exit()
    return


def update_play_table(val, ce):
    play_table.pop(val)
    play_table.insert(int(val), ce)
    return play_table


def comp_play(POI):
    print('comp move now')
    # comp_move = ''
    if len(POI_0) != 0:
        comp_move = 4
    elif len(POI_1) != 0:
        comp_move = choice(POI_1) - 1
    else:
        comp_move = choice(POI_2) - 1
    return comp_move


def block_player():
    a = play_table[:3]
    b = play_table[3:6]
    c = play_table[6:]
    d = play_table[0], play_table[3], play_table[6]  # [a1, b1, c1]
    e = play_table[1], play_table[4], play_table[7]  # [a2, b2, c2]
    f = play_table[2], play_table[5], play_table[8]  # [a3, b3, c3]
    g = play_table[0], play_table[4], play_table[8]  # [a1, b2, c3]
    h = play_table[2], play_table[4], play_table[6]  # [a3, b2, c1]
    tot = [a, b, c, d, e, f, g, h]
    comp_move = ''
    for item in tot:
        x = item.count('X')
        y = item.count('O')
        if y == 2 and x == 0:
            for v in item:
                if v != 'O':
                    comp_move = int(v) - 1
        elif x == 2 and y == 0:
            for v in item:
                if v != 'X':
                    comp_move = int(v) - 1

    return comp_move


def game_tie(num_played):
    if len(num_played) == 9:
        print(f'Remiza')
        print_table()
        exit()


while True:
    ########################## Human move
    print_table()
    user_val = user_input(num_played)
    update_play_table(user_val, user_mark)
    update_POI(POI, user_val)
    who_win(play_table)
    game_tie(num_played)
    ########################### Comp move
    x = block_player()
    if x == '':
        comp_move = comp_play(POI)
        num_played.append(comp_move)
    else:
        comp_move = x
        num_played.append(comp_move)
    update_play_table(comp_move, comp_mark)
    update_POI(POI, comp_move)
    who_win(play_table)
    game_tie(num_played)