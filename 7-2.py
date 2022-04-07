class Clothes:
    pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            self.__size = 40
        elif size > 60:
            self.__size = 60
        else:
            self.__size = size

    def cloth(self):
        #print(self.__size)
        return self.__size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 150:
            self.__height = 150
        elif height > 210:
            self.__height = 210
        else:
            self.__height = height

    def cloth(self):
        #print(self.__height)
        return 2 * self.__height + 0.3


c = Coat(float(input("Введите размер пальто: ")))
a = c.cloth()
print("Для пальто: ", a)
s = Suit(float(input("Введите рост для костюма: ")))
b = s.cloth()
print("Для костюма: ", b)
print("Итого: ", a + b)
