v = float(input("Введите выручку:"))
i = float(input("Введите издержки:"))
if v > i:
    print("Прибыльно")
    print("Рентабельность:%f" % (((v - i) / v) * 100))
    per = int(input("Введите кол-во сотрудников в фирме:"))
    print ("Прибыль на каждого: %f" % ((v-i)/per))
else:
    print("Убыточно")
