my_file = open("for_5-4.txt", "r", encoding="utf-8")
new_file = open("for_5-4_new.txt", "w", encoding="utf-8")
my_file.seek(0)
b = ["Один", "Два", "Три", "Четыре"]
str_line = 0
for line in my_file:
    new_file.write(b[str_line] + line.split()[1] + line.split()[2] + '\n')
    str_line += 1
my_file.close()
new_file.close()
