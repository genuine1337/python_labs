def transpose(mat: list[list[float | int]]) -> list[list]:
    """
    На вход подаётся матрица размера m*n,
    где m - число строк, n - число столбцов.
    Возвращается матрица размера n*m,
    т.е. строки и столбцы меняются местами.
    Для пустой матрицы: [] -> [].
    Если строки в матрице разной длины(рваная матрица), то
    вернется ValueError.
    """
    if mat == []:
        return []
    
    for row in mat:
        if len(row) != len(mat[0]):
            raise ValueError("Рваная матрица")

    rows = len(mat)
    columns = len(mat[0])
    result = []

    for j in range(columns):
        result.append([])

    for i in range(rows):
        for j in range(columns):
            result[j].append(mat[i][j])
    return result

# print(transpose([[1, 2], [3]]))

def row_sums(mat: list[list[float | int]]) -> list[float]:
    """
    На вход подаётся матрица из m строк.
    Если во всех строках одинаковое число элементов,
    для каждой строки вернётся сумма её элементов.
    Если строки в матрице разной длины,
    вернётся ValueError.
    """
    for row in mat:
        if len(row) != len(mat[0]):
            raise ValueError("Рваная матрица")
        
    result = []
    for row in mat:
        result.append(sum(row))
    return result

def col_sums(mat: list[list[float | int]]) -> list[float]:
    """
    На вход подаётся матрица из m строк.
    Если во всех строках одинаковое число элементов,
    для каждого столбца матрицы вернётся сумма его элементов.
    Если строки в матрице разной длины,
    вернётся ValueError.
    """

    for row in mat:
        if len(row) != len(mat[0]):
            raise ValueError("Рваная матрица")
    res = []
    row_len = len(mat[0])