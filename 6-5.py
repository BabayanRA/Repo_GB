class Stationery:
    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручка")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандаш")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркер")


Stationery().draw()
Pen().draw()
Pencil().draw()
Handle().draw()
