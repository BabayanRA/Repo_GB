def sum_number():
    summa = 0
    str_number = ""
    while str_number != "=":
        str_number = input("Строка чисел через пробел или '=' для окончательного расчета:")
        for i in range(0, len(str_number.split())):
            if str_number.split()[i] != "=":
                summa = summa + float(str_number.split()[i])
            else:
                str_number = "="
                break
                return print(summa)
        print(summa)


sum_number()
