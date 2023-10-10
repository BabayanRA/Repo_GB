from functools import reduce


def summa_func(prev_j, j):
    return prev_j + j


my_file = open("for_5-5.txt", "w+", encoding="utf-8")
my_file.writelines("1.1 2.2 3.4 4.6 5.8 6.9")
my_file.seek(0)
a = my_file.readline().split()
my_file.close()
list_for_sum = [float(el) for el in a]
summa = 0
for i in a:
    summa += float(i)
print("Сумма через переменную summa: ", summa)
print("Сумма через функцию sum(): ", sum(list_for_sum))
print("Сумма через функцию reduce(): ", reduce(summa_func, list_for_sum))
