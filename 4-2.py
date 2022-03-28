def my_func(my_list):
    for i in range(0, len(my_list) - 1):
        if my_list[i] < my_list[i + 1]:
            yield my_list[i + 1]


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([el for el in my_func(my_list)])
