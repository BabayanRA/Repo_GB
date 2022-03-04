n = abs(int(input("Введите число: ")))
max_ = 0
ost = 0
while (n / 10) != 0:
    ost = n % 10
    if ost > max_:
        max_ = ost
    n = n // 10
print(max_)
