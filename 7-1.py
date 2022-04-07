class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % k for k in row]) for
                          row in self.matrix])

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] += other.matrix[i][j]
        return Matrix(self.matrix)


m_1 = Matrix([[31, 32], [37, 43], [51, 86]])
m_2 = Matrix([[49, 68], [33, 77], [9, 4]])
print(m_1)
print("_______________________________")
print(m_2)
print("_______________________________")
print(m_1 + m_2)
