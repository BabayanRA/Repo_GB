class Data:
    def __init__(self, day, month, year):
        # self.day = data.split("-")[0]
        # self.month = data.split("-")[1]
        # self.year = data.split("-")[2]
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def data_preobr(cls, data):
        try:
            day = int(data.split("-")[0])
            month = int(data.split("-")[1])
            year = int(data.split("-")[2])
        except ValueError:
            return "Введите правильное значение даты"
        if (cls.validation(day, month, year) == False):
            return "Введите правильное значение даты"
        else:
            return cls(day, month, year)

    def __str__(self):
        return f"Число: {self.day}, Месяц: {self.month}, Год: {self.year}"

    @staticmethod
    def validation(day, month, year):
        if (day > 31) or (day < 1):
            print("Число дня от 1 до 31")
            if (month > 12) or (month < 1):
                print("Число месяца от 1 до 12")
                if (year > 9999) or (year < 1):
                    print("Число года от 1 до 9999")
                    return False


a = input("Введите дату в формате ДД-ММ-ГГГГ (0 < ДД < 31, 0 < ММ < 12, 0 < ГГГГ < 9999): ")
d = Data.data_preobr(a)
print(d)
