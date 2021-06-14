from operator import add, sub, mul, truediv
operator = {'+': add, '-': sub, '*': mul, '/': truediv}


def get_numar(i) -> int:
    numar = None
    while True:
        try:
            numar = input("Introduceti cifra: ")
            numar = int(numar)
            if i == 2 and operator_in == '/' and numar == 0:
                print('Nu se pot face impartiri la 0. Introduceti alt numar: ')
                continue
            break
        except ValueError:
            if numar == "q":
                exit()
            print('Introduceti doar cifre: ')
            continue
    return numar


def get_operator_in() -> str:
    operator_in = None
    while True:
        try:
            operator_in = input("Introduceti operatorul (+, -, *, /): ")
            list_oper = ('+', '-', '*', '/')
            if operator_in in list_oper:
                break
            else:
                print('Introduceti doar operatori (+, -, *, /): ')
                continue
        except ValueError:
            print('Eroare')
            continue
    return operator_in


while True:
    i = 1
    a = get_numar(i)
    operator_in = get_operator_in()
    i = i + 1
    b = get_numar(i)
    print(operator[operator_in](a, b))
    print('Press \'q\' for exit')