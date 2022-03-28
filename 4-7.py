import math


def fact(n):
    for i in range(1, n + 1):
        yield math.factorial(i)


print([el for el in fact(int(input("Число: ")))])