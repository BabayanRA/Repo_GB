class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        a = abs(self.num - other.num)
        if a != 0:
            return Cell(a)
        else:
            return "Разность равна нулю"

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def __str__(self):
        return f"New Cell, number of cell: {self.num}"

    def make_order(self, num_order):
        a = divmod(self.num, num_order)
        return ('*' * num_order + '\n') * a[0] + '*' * a[1]


c1 = Cell(3)
c2 = Cell(14)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(Cell.make_order(c1, 5))
print("_________________________________________________")
print(Cell.make_order(c2, 5))
