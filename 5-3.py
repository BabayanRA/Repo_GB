my_file = open("for_5-3.txt", "r", encoding="utf-8")
my_file.seek(0)
str_file = 0
summa = 0
print("Оклад < 20000: ")
for line in my_file:
    str_file += 1
    if float(line.split()[1]) < 20000:
        print(line.split()[0])
    summa += float(line.split()[1])
print("Cредний заработок: ", summa / str_file)
my_file.close()
