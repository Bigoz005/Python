# Poprawność numeru bankowego
"""
Numer konta ma być generowany przez program

Badanie poprawnosci numeru rachunku bankowego NRB mozna sprawdzic tak:
1.
do numeru konta dopisac z prawej strony ciag 2521, ktory odpowiada kodowi literowemu PL (P - 25, L -21)
2.
liczbe kontrolna(pierwsze dwie cyfry numeru NRB) nalezy przeniesc na koniec ( z lewej na prawa)
3.
uzyskany ciag liczb podzielic modulo 97

Jezeli reszta z dzielenia wynosi 1, to numer NRB jest poprawny
"""

import re
import math
import random


def randrandrand():
    n = 26
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    number = random.randint(range_start, range_end)
    return number


print("Press 1 if you want to write your bank account number")
test = input()
if test == 1:
    print('Enter the number: ')
    x = input()
    x = x.replace(' ', '')
    x = x.replace('-', '')
    if len(x) != 26:
        print("Error: wrong lenght of number"), exit(1)
    if re.search('[a-zA-Z]', x):
        print("Error: invalid character"), exit(1)
    x += '2521'
    x += x[0] + x[1]
    x = x[2:]
    y = float(x)
    z = math.fmod(y, 97)
    if z == 1:
        print("Correct number"), exit(0)
    else:
        print("Incorrect number"), exit(1)
else:
    w = randrandrand()
    print("Generate by function")
    if len(w) != 26:
        print("Error: wrong lenght of number"), exit(1)
    if re.search('[a-zA-Z]', w):
        print("Error: invalid character"), exit(1)
    w += '2521'
    w += w[0] + w[1]
    w = x[2:]
    r = float(w)
    z = math.fmod(r, 97)
    if z == 1:
        print("Correct number"), exit(0)
    else:
        print("Incorrect number"), exit(1)

