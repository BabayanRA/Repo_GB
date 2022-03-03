a = float(input("Введите 1-ую пробежку:"))
b = float(input("Введите желаемый километраж:"))
day = 1
while a < b:
    a = a + (a / 10)
    day += 1
    print("Day %d:%.2f км" % (day, a))
