class NoNumberEx(Exception):
    def __init__(self, str_num):
        self.str_num = str_num

    def __str__(self):
        return f"Вводить можно только числа, '{self.str_num}' - не записано"


""" # Решение через Comprehension (начало)
    def my_func(self):
        s = ''
        sp = self.str_num.split()
        for i in range(0, len(sp)):
            s = sp[i].replace(".", '').replace('-', '')
            try:
                if s.isnumeric() is True:
                    yield float(sp[i])
                else:
                    raise NoNumberEx(sp[i])
            except NoNumberEx as err:
                print(err)


b = []
a = ''
while True:
    a = input("Введите число (для окончания ввода введите 'stop'): ")
    if a != 'stop':
        b.append([el for el in NoNumberEx(a).my_func()])
    else:
        print("Решение через Comprehension:")
        for i in range(0, len(b)):
            for j in range(0, len(b[i])):
                print(b[i][j], end=' ')
        break
""" # Решение через Comprehension (конец)

#""" # Решение через обычный список (начало)
b = []
a = ''
while True:
    a = input("Введите число (для окончания ввода введите 'stop'): ")
    if a != 'stop':
        s = ''
        sp = a.split()
        for i in range(0, len(sp)):
            s = sp[i].replace(".", '').replace('-', '')
            try:
                if s.isnumeric() is True:
                    b.append(float(sp[i]))
                else:
                    raise NoNumberEx(sp[i])
            except NoNumberEx as err:
                print(err)
    else:
        print("Вывод списком:", b)
        break
#""" # Решение через обычный список (конец)
