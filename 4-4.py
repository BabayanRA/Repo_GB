def my_func(my_list):
    for i in range(0, len(my_list)):
        if my_list.count(my_list[i]) == 1:
            yield my_list[i]


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([el for el in my_func(my_list)])
