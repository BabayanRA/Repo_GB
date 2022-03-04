time = float(input("Введите число: "))
print(time)
sec = time % 60
mt = (time / 60) % 60
h = time // 3600
print("Дата: %02.0f:%02.0f:%02.0f" % (h, mt, sec))
print(f"Дата: {h:02.0f}:{mt:02.0f}:{sec:02.0f}")  # разные варианты вывода данных
print("Дата: {0:02.0f}:{1:02.0f}:{2:02.0f}".format(h, mt, sec))
