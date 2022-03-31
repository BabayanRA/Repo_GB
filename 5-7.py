import json


def my_dictionary(file):
    for line in file:
        yield line.split()[0], float(line.split()[2]) - float(line.split()[3])


def average_profit_func(dict_firm):
    summa = 0
    firm_ub = 0
    for i in dict_firm.values():
        if i >= 0:
            summa += i
        else:
            firm_ub += 1
    return summa / (len(dict_firm) - firm_ub)


my_file = open("for_5-7.txt", "r", encoding="utf-8")
my_file.seek(0)
my_dict = {key: value for key, value in my_dictionary(my_file)}
my_file.close()
average_profit = {"average_profit": average_profit_func(my_dict)}
with open("for_5-7_new.json", "w", encoding="utf-8") as my_json:
    json.dump([my_dict, average_profit], my_json, ensure_ascii=False, indent=4)
