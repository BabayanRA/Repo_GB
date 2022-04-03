class Worker:
    def __init__(self, n, sn, pos, wage, bonus):
        self.name = n
        self.surname = sn
        self.position = pos
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(sum(self._income.values()))


p = Position(n=input("Name: "), sn=input("Surname: "), pos=input("Position: "), wage=float(input("Wage: ")),
             bonus=float(input("Bonus: ")))
#p = Position(n="Ivan", sn="Petrov", pos="35", wage=12500.0, bonus=5000.0)
p.get_full_name()
p.get_total_income()
