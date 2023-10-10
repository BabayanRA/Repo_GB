from sys import argv
from itertools import count, cycle

name, n = argv

for i in count(int(n)):
    if i > 10:
        break
    else:
        print(i)

print("_______________________________________________________________________________________________________________")
# _______________________________________________________________________________________________________________________
a = 0
my_list = ["Python", "Java", "C++"]
for i in cycle(my_list):
    if a > 5:
        break
    else:
        print(i)
        a += 1
