def string_1():
    my_str = input("Введите cтроку со словами с маленькой буквы через пробел: ")

    str1 = my_str.capitalize()
    str2 = ""
    for i in range (0, len(my_str.split())):
        if i < (len(my_str.split()) - 1):
            str2 = str2 + my_str.split()[i].capitalize() + " "
        else:
            str2 = str2 + my_str.split()[i].capitalize()
    return print(str1), print(str2)


string_1()
