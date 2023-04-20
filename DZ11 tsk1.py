class Matrix:
    def init(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [0 for j in range(cols) for i in range(rows)]

    def str(self):
        return '\n'.join(' '.join([str(self.matrix[ij) for j in range(self.cols)]) for i in range(self.rows)])

    def eq(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrixij != other.matrixij:
                    return False
        return True

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Matrices must have the same dimensions')
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrixij = self.matrixij + other.matrixij
        return result



A = Matrix(2, 3)
A.matrix = [[1, 2, 3], [4, 5, 6]]
print(A)

B = Matrix(2, 3)
B.matrix = [[1, 2, 3], [4, 5, 6]]
print(B)

C = Matrix(2, 2)
C.matrix = [[1, 2], [3, 4]]
print(C)

D = Matrix(3, 2)
D.matrix = [[1, 2], [3, 4], [5, 6]]
print(D)

print(A == B)
print(A == C)

print(A + B)

print(C,  D)