def func_del(x, y):
    if y != 0:
        return x / y
    else:
        return "Деление на ноль невозможно"


num1 = float(input("Делимое:"))
num2 = float(input("Делитель:"))
print(func_del(num1, num2))
