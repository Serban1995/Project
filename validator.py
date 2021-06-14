import datetime
# 1690726424525
Judete = {'01': 'Alba',
              '02': 'Arad',
              '03':	'Argeș',
              '04':	'Bacău',
              '05':	'Bihor',
              '06':	'Bistrița-Năsăud',
              '07':	'Botoșani',
              '08':	'Brașov',
              '09':	'Brăila',
              '10':	'Buzău',
              '11':	'Caraș-Severin',
              '12':	'Cluj',
              '13':	'Constanța',
              '14':	'Covasna',
              '15':	'Dâmbovița',
              '16':	'Dolj',
              '17':	'Galați',
              '18':	'Gorj',
              '19':	'Harghita',
              '20':	'Hunedoara',
              '21':	'Ialomița',
              '22':	'Iași',
              '23':	'Ilfov',
              '24':	'Maramureș',
              '25':	'Mehedinți',
              '26':	'Mureș',
              '27':	'Neamț',
              '28':	'Olt',
              '29':	'Prahova',
              '30':	'Satu Mare',
              '31':	'Sălaj',
              '32':	'Sibiu',
              '33':	'Suceava',
              '34':	'Teleorman',
              '35':	'Timiș',
              '36':	'Tulcea',
              '37':	'Vaslui',
              '38':	'Vâlcea',
              '39':	'Vrancea',
              '40':	'București',
              '41':	'București - Sector 1',
              '42':	'București - Sector 2',
              '43':	'București - Sector 3',
              '44':	'București - Sector 4',
              '45':	'București - Sector 5',
              '46':	'București - Sector 6',
              '51':	'Călărași',
              '52':	'Giurgiu',
              '47':	'Bucuresti - Sector 7 (desfiintat)',
              '48':	'Bucuresti - Sector 8 (desfiintat)'}

CRC = 279146358279

while True:
    try:
        cnp_in = int(input("Introduceti CNP: "))
        if len(str(cnp_in)) != 13:
            print('Introduceti 13 cifre')
            continue
        else:
            break
    except ValueError:
        print('Introduceti doar cifre')
#  1690726424525

# CNP_list = [int(x) for x in str(cnp_in)]
CNP_list = list(str(cnp_in))

an = CNP_list[1:3]
s = [str(i) for i in an]
result = str("".join(s))
an = int(result)

luna = CNP_list[3:5]
s = [str(i) for i in luna]
result = str("".join(s))
luna = int(result)

zi = CNP_list[5:7]
s = [str(i) for i in zi]
result = str("".join(s))
zi = int(result)

sex = int(CNP_list[0])

Judet = CNP_list[7:9]
s = [str(i) for i in Judet]
Judet = str("".join(s))

interval = CNP_list[9:12]
s = [str(i) for i in interval]
result = str("".join(s))
interval = int(result)

if sex == 9:
    print('Persoana straina')
elif sex == 1 or sex == 2:
    try:
        data_de_comparat = datetime.datetime(int(f"19{an}"), luna, zi)
        # print(type(data_de_comparat))
        if sex == 1 and datetime.datetime(1900, 1, 1) < data_de_comparat < datetime.datetime(1999, 12, 31):
            print(f"Sex barbatesc nascut in intervalul 1900 - 1999 in luna {luna} ziua {zi}")
        else:
            if sex == 2 and datetime.datetime(1900, 1, 1) < data_de_comparat < datetime.datetime(1999, 12, 31):
                print(f"Sex femeiesc, nascuta in intervalul 1900 - 1999 in luna {luna} ziua {zi}")
    except ValueError:
        print("Ziua nu este valida")
elif sex == 3 or sex == 4:
    try:
        data_de_comparat = datetime.datetime(int(f"18{an}"), luna, zi)
        if sex == 3 and datetime.datetime(1800, 1, 1) < data_de_comparat < datetime.datetime(1899, 12, 31):
            print(f"Sex barbatesc nascut in intervalul 1800 - 1899 in luna {luna} ziua {zi}")
        else:
            if sex == 4 and datetime.datetime(1800, 1, 1) < data_de_comparat < datetime.datetime(1899, 12, 31):
                print(f"Sex femeiesc nascuta in intervalul 1800 - 1899 in luna {luna} ziua {zi}")
    except ValueError:
        print("Ziua nu este valida")
elif sex == 5 or sex == 6:
    try:
        data_de_comparat = datetime.datetime(int(f"20{an}"), luna, zi)
        if sex == 5 and datetime.datetime(2000, 1, 1) < data_de_comparat < datetime.datetime(2099, 12, 31):
            print(f"Sex femeiesc nascut in intervalul 2000 - 2099 in luna {luna} ziua {zi}")
        else:
            if sex == 6 and datetime.datetime(2000, 1, 1) < data_de_comparat < datetime.datetime(2099, 12, 31):
                print(f"Sex femeiesc nascuta in intervalul 2000 - 2099 in luna {luna} ziua {zi}")
    except ValueError:
        print("Ziua nu este valida")
else:
    print("Persoana straina, rezidenta in Romanaia")

if 1 < int(Judet) <= 39:
    print(f'Numarul {interval} a fost alocat in biroul de evidenta al judetului', Judete[Judet])
else:
    print(f'Numarul {interval} a fost alocat in biroul de evidenta al Municipiului', Judete[Judet])

# 1690726424525
# aici calculam cifra de control (cifrele sunt pentru CNP-ulmeu. SA NU LUATI CREDIE IN NUMELE MEU :))


# CNP_list = list(str(cnp_in))
CNP_list = [int(x) for x in str(cnp_in)]  # transformam int in list [1, 6, 9, 0, 7, 2, 6, 4, 2, 4, 5, 2, 5]
CNP_list_mic = CNP_list[:-1]
# print(CNP_list_mic)
# print(type(CNP_list_mic))


CRC_list = [int(x) for x in str(CRC)] # transformam int in list [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
print(CRC_list)
print(type(CRC_list))


zipped_lists = zip(CNP_list_mic, CRC_list)
multiplication = [x * y for (x, y) in zipped_lists]  # [2, 42, 81, 0, 28, 12, 18, 20, 16, 8, 35, 18]
suma = sum(multiplication)                          # 280
print(suma)
control_number = suma % 11
CN = 0
if control_number == 10:
    CN = 1
else:
    CN = control_number
                                        # se verifica daca val cnp fara ultima cifra functioneaza
if CN == CNP_list[-1]:
    print(f'CNP-ul {cnp_in} este valid')
else:
    print('CNP GRESIT')