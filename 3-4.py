def x_degree(num1, num2):

    """
    Возведение в степень

    Именнованные параметры
    num1, a - число
    num2, b - степень

    """

    while True:
        num1 = input("Действительное число (>0):")
        try:
            if float(num1) > 0:
                break
        except ValueError or TypeError:
            num1 = 0
    a = float(num1)
    while True:
        num2 = input("Целое число (<0):")
        try:
            if int(num2) < 0:
                break
        except ValueError or TypeError:
            num2 = 0
    b = int(num2)
    result_for = a
    for i in range(0, abs(b) + 1):
        result_for = result_for / a
    return print("Через POW:", pow(a, b)), print("Через цикл FOR:", result_for)


x_degree(num1=0, num2=0)
