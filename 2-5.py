my_list = [7, 5, 3, 3, 2]
print(my_list)
while (input("Выбор ('Enter' - ввести значение, '-' + 'Enter' - закончить ввод): ")) != "-":
    a = int(input("Введите значение:"))
    for i in range(len(my_list)):
        if a > my_list[i]:
            my_list.insert(i, a)
            break
        if a <= my_list[len(my_list) - 1]:
            my_list.append(a)
            break
    print(my_list)
