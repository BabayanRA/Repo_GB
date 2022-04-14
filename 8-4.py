class Warehouse:

    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.lists = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Имя': self.name, 'Цена': self.price, 'Шт': self.quantity}

    def supply(self):
        try:
            unit = input(f"Введите наименование: ")
            unit_p = int(input(f"Введите цену за ед: "))
            unit_q = int(input(f"Введите количество: "))
            unique = {'Имя:': unit, 'Цена:': unit_p, 'Шт:': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f"Текущий список: \n {self.my_store}")
        except:
            return "Ошибка ввода данных"

        print(f"Для выхода - Q, продолжение - Enter")
        q = input(f"---> ")
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f"Весь склад: \n {self.my_store_full}")
            return "Выход"
        else:
            return Warehouse.supply(self)


class Printer(Warehouse):
    def printer_use(self):
        return f"Распечатано {self.lists} листов"


class Scanner(Warehouse):
    def scanner_use(self):
        return f"Отсканировано {self.lists} листов"


class Xerox(Warehouse):
    def xerox_use(self):
        return f"Скопировано {self.lists} листов"


p = Printer('HP', 5000, 6, 12)
s = Scanner('Canon', 1500, 8, 9)
x = Xerox('Xerox', 2000, 3, 18)

print(p.supply())

print(p.printer_use())
print(s.scanner_use())
print(x.xerox_use())
