class Car:
    def __init__(self, n, c, sp, p):
        self.name = n
        self.color = c
        self.speed = sp
        self.ispolice = p
        # self.direction = d

    def go(self):
        print("Машина едет")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Скорость:{self.speed} км/ч")

    def is_pc(self):
        if self.ispolice == True:
            print ("Это полицейская машина")
        else:
            print ("Это не полицейская машина")
class TownCar(Car):
    def show_speed(self):
        if float(self.speed) > 60:
            print("Превышение скорости! Максимально разрешенная скорость - 60 км/ч")
        else:
            print(f"Скорость:{self.speed} км/ч")


class WorkCar(Car):
    def show_speed(self):
        if float(self.speed) > 40:
            print("Превышение скорости! Максимально разрешенная скорость - 40 км/ч")
        else:
            print(f"Скорость:{self.speed} км/ч")


class SportCar(Car):
    def price(self):
        print("Данный авто стоит 300.000$")


class PoliceCar(Car):
    def police(self):
        print(f"{self.name} ведет преследование на скорости {self.speed} км/ч")


t = TownCar(n="Городской авто", c="Белый", sp=float(input("Введите скорость для городского авто (км/ч): ")), p=False)
print(f"Тип: {t.name}", f"Цвет: {t.color}", sep="\n")
t.is_pc()
t.go()
t.show_speed()
t.turn(input("Введите направление поворота: "))
t.stop()
w = WorkCar(n="Рабочий авто", c="Серый", sp=float(input("Введите скорость для рабочего авто (км/ч): ")), p=False)
print(f"Тип: {w.name}", f"Цвет: {w.color}", sep="\n")
w.is_pc()
w.go()
w.show_speed()
w.turn(input("Введите направление поворота: "))
w.stop()
s = SportCar(n="Городской авто", c="Красный", sp=float(input("Введите скорость для спортивного авто (км/ч): ")),
             p=False)
print(f"Тип: {s.name}", f"Цвет: {s.color}", sep="\n")
s.price()
s.is_pc()
s.go()
s.show_speed()
s.turn(input("Введите направление поворота: "))
s.stop()
pc = PoliceCar(n="Полицейский авто", c="Полицейский",
               sp=float(input("Введите скорость для полицейского авто (км/ч): ")), p=True)
print(f"Тип: {pc.name}", f"Цвет: {pc.color}", sep="\n")
pc.is_pc()
pc.go()
pc.show_speed()
pc.police()
pc.turn(input("Введите направление поворота: "))
pc.stop()
