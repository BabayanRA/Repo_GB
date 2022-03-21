def found_sum_max(a, b, c):
    list_num = [a, b, c]
    list_num.remove(min(list_num))
    return sum(list_num)


num1 = float(input("Число 1:"))
num2 = float(input("Число 2:"))
num3 = float(input("Число 3:"))
print(found_sum_max(num1, num2, num3))
