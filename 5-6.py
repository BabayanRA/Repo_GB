def my_dictionary(file):
    for line in file:
        summa = 0
        for i in range(1, len(line.split())):
            try:
                summa += int(line.split()[i][:line.split()[i].index("("):])
            except ValueError:
                summa += 0
        yield line.split()[0][:-1:], summa


my_file = open("for_5-6.txt", "r", encoding="utf-8")
my_file.seek(0)
my_dict = {key: value for key, value in my_dictionary(my_file)}
my_file.close()
print(my_dict)
