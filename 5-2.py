my_file = open("for_5-2.txt", "r", encoding="utf-8")
my_file.seek(0)
str_file = 0
word_file = 0
for line in my_file:
    str_file += 1
    for i in line.split():
        word_file += 1
my_file.close()
print(str_file, word_file)
