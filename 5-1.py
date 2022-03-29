my_file = open("for_5-1.txt", "w+", encoding="utf-8")
while True:
    a = input("Введите строку (для окончания ввода введите символ в новой строке '-'): ")
    if a != "-":
        my_file.writelines(a + "\n")
    else:
        break
my_file.writelines("")
my_file.close()
