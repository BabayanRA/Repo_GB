month = int(input("Введите число месяца: "))
if (month > 12) or (month < 1):
    print("Такого месяца не существует")
k = 0
my_list = ["Зима", "Весна", "Лето", "Осень"]
my_dict = {"Зима": [1, 2, 3], "Весна": [4, 5, 6], "Лето": [7, 8, 9], "Осень": [10, 11, 12]}
my_list2 = ["Зима", [1, 2, 3], "Весна", [4, 5, 6], "Лето", [7, 8, 9], "Осень", [10, 11, 12]]
for i, el in enumerate(my_dict.values(), 1):
    # print(f"{i}) {el}")
    for k in range(len(el)):
        if el[k] == month:
            for j, time_year in enumerate(my_dict.keys(), 1):
                # print(f"{j}) {time_year}")
                if i == j:
                    print(time_year)
# _______________________________________________________________________________________________________________
print("__________________________________________________________________________________________________________")
if month in range(1, 4):
    print(my_list[0])
elif month in range(4, 7):
    print(my_list[1])
elif month in range(7, 10):
    print(my_list[2])
elif month in range(10, 13):
    print(my_list[3])
# _______________________________________________________________________________________________________________
print("__________________________________________________________________________________________________________")
for i in range(int(len(my_list2)/2)):
    i = 2*i + 1
    for k in range(len(my_list2[i])):
        if my_list2[i][k] == month:
            print(my_list2[i-1])
