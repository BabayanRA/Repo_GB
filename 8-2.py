class ZeroDivisionEx(Exception):
    def __str__(self):
        return "На ноль делить нельзя"


a = float(input("Делимое: "))
b = float(input("Делитель: "))
try:
    if b == 0:
        raise ZeroDivisionEx()
    else:
        print(a/b)
except ZeroDivisionEx as err:
    print(err)

