month = int(input("Введите число месяца: "))
k = 0
my_list = ["Зима", "Весна", "Лето", "Осень"]
my_dict = {"Зима": [1, 2, 3], "Весна": [4, 5, 6], "Лето": [7, 8, 9], "Осень": [10, 11, 12]}

for i in my_dict.keys():
    if my_dict.get(i)[k] == month:
        print(my_dict.get())
