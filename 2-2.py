my_list = []
while (input("Выбор ('Enter' - ввести значение, '-' + 'Enter' - закончить ввод): ")) != "-":
    my_list.append(input("Введите эл списка:"))
print(my_list)
i = 0
for el in range(int(len(my_list) / 2)):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i = i + 2
print(my_list)
