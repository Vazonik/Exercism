class Matrix:
    def __init__(self, matrix_string):
        self.rows = [[int(j) for j in i.split(" ")] for i in matrix_string.split("\n")]
        self.columns = [list(i) for i in zip(*self.rows)]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]
