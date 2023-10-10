from sys import argv

name, vyrabotka, stavka, premiya = argv
try:
    print(float(vyrabotka) * float(stavka) + float(premiya))
except ValueError or TypeError:
    print("Необходимо вводить числа")


