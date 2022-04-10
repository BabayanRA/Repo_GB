class CNum:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        return CNum(self.num1 + other.num1, self.num2 + other.num2)

    def __mul__(self, other):
        return CNum(
            (self.num1 * other.num1 - self.num2 * other.num2), (self.num1 * other.num2 - (-1) * other.num1 * self.num2))

    def __str__(self):
        if (self.num1 == 0) and (self.num2 == 0):
            return f"{self.num1}"
        elif self.num1 == 0:
            return f"{self.num2}j"
        elif self.num2 == 0:
            return f"{self.num1}"
        elif self.num2 > 0:
            return f"{self.num1}+{self.num2}j"
        else:
            return f"{self.num1}-{(-1) * self.num2}j"


a = CNum(2, 3)
b = CNum(4, 5)
print(a)
print(b)
print(a + b)
print(a * b)
