import numpy as np
from scipy import linalg
from sympy import symbols, Eq, solve, solve_linear_system, Matrix

def transpose(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result

def arrscalarProduct(array, k):
    for i in range(len(array)):
        array[i] = array[i] * k 
    return array

def multiply(matrix1, matrix2):
    # syarat digunakan : ukuran matrix1 dan matrix2 mengikuti kaidah perkalian matriks dan menghasilkan matriks result
    resultrow = len(matrix1)
    resultcol = len(matrix2[0])
    result = [[0 for j in range(resultcol)] for i in range((resultrow))]
    for i in range(resultrow):
        for j in range(resultcol):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def minormatrix(matrix, i, j):
    # mendapatkan minor matrix dengan menghilangkan row i dan kolom j
    return [row[: j] + row[j+1:] for row in (matrix[: i] + matrix[i+1:])]
 
 
def determinant(matrix):
    # basis rekursi : matriks 2x2
    if(len(matrix) == 2):
        det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return det

    det = 0
    
    # penghitungan determinan matriks menggunakan kofaktor
    for col in range(len(matrix)):
        det_minor = determinant(minormatrix(matrix, 0, col))
        cofactor = (-1)**(col) * det_minor
        det += matrix[0][col] * cofactor

    return det

def subtract(matrix1, matrix2):
    mat = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1))] for i in range(len(matrix1))]
    return mat

# def eigenvalue(matrix):
#     x = symbols('x')
#     lambda_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix))]
#     for i in range(len(matrix)):
#         lambda_matrix[i][i] = x
#     mat = subtract(matrix, lambda_matrix)

#     eq1 = Eq(determinant(mat), 0)
#     sol = solve(eq1)
#     return sol

# def eigenvectors(matrix, eigenval):
#     eigenvectors = []
#     lambda_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix))]
#     # nil_matrix = [0 for i in range(len(matrix))]
#     for val in eigenval:
#         for k in range(len(matrix)):
#             lambda_matrix[k][k] = val       
#             res_matrix = subtract(matrix, lambda_matrix)
#         for row in range(len(res_matrix)):
#             res_matrix[row].append(0)

#         system = Matrix(res_matrix)

#         x,y,z = symbols('x y z')
#         vector = solve_linear_system(system, x, y, z)
#         eigenvectors.append(vector)
#     return eigenvectors

def eigenvalue(matrix):
    m = np.array(matrix)
    w, v = np.linalg.eig(m)
    w = w.tolist()
    rounded = [round(num, 2) for num in w]
    return rounded

def eigenvectors(matrix):
    m = np.array(matrix)
    w, v = np.linalg.eig(m)
    v = v.tolist()
    rounded = [[0 for j in range(len(v[0]))] for i in range(len(v))]
    for i in range(len(v)):
        for j in range(len(v[0])):
            rounded[i][j] = round(v[i][j], 2)
    return rounded

def sigmavalue(matrix):
    sigma_val = []
    eigen_val = eigenvalue(matrix)
    for val in eigen_val:
        if val != 0:
            sigma_val.append(val**(0.5))
    return sigma_val

def sigma_matrix(matrix):
    ata = multiply(transpose(matrix), matrix)
    sigma_val = sigmavalue(ata)
    row = len(matrix)
    col = len(matrix[0])
    mat = [[0 for j in range(col)] for i in range(row)]

    for i in range(len(sigma_val)):
        mat[i][i] = round(sigma_val[i], 2)
    return mat

def vtrans_matrix(matrix):
    ata = multiply(transpose(matrix), matrix)
    return eigenvectors(ata)

def u_matrix(matrix):
    mat = []
    ata = multiply(transpose(matrix), matrix)
    sigma_val = sigmavalue(ata)
    for i in range(len(sigma_val)):
        multiplyres = np.array(matrix).dot(np.array(vtrans_matrix(matrix)[i])).tolist()
        k = 1/sigma_val[i]
        u_mat = arrscalarProduct(multiplyres, k)
        rounded = [round(num, 2) for num in u_mat]
        mat.append(rounded)
    return mat

matrix1 = [[2,0,8,6,0], [1,6,0,1,7], [5,0,7,4,0], [7,0,8,5,0], [0,10,0,0,7]]
ata = multiply(transpose(matrix1), matrix1)
print(ata)
print(u_matrix(matrix1))
print(sigma_matrix(matrix1))
print(vtrans_matrix(matrix1))
# mat = multiply(u_matrix(matrix1), sigma_matrix(matrix1))
# print(multiply(mat, vtrans_matrix(matrix1)))


# a = np.array([[5, 3, 0], [3, 5, 0], [0, 0, 0]])
# b = np.array([0, 0, 0])
# x = np.linalg.solve(a, b)
# print(x)