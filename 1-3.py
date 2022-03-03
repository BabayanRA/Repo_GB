n = input("Введите целое положительное число: ")
while int(n)<0:
    n = input("Введите целое положительное число: ")
print(int(n) + int(n + n) + int(n + n + n))
