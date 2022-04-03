class Road:
    def __init__(self, l_r, w_r):
        self._len = l_r
        self._width = w_r

    def result_m(self):
        result = float(self._len) * float(self._width) * 25 * 5 / 1000
        print(result, "т")


r = Road(input("Длина(м): "), input("Ширина(м): "))
r.result_m()
