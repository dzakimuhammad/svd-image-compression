import numpy as np

def transpose(matrix):
    return np.transpose(matrix)

def arrscalarProduct(array, k):
    for i in range(len(array)):
        array[i] = array[i] * k 
    return array

def multiply(matrix1, matrix2):
    # syarat digunakan : ukuran matrix1 dan matrix2 mengikuti kaidah perkalian matriks dan menghasilkan matriks result
    resultrow = len(matrix1)
    resultcol = len(matrix2[0])
    result = [[0 for j in range(resultcol)] for i in range(resultrow)]
    for i in range(resultrow):
        for j in range(resultcol):
            for k in range(len(matrix2)):
                result[i][j] += int(matrix1[i][k]) * int(matrix2[k][j])
    return np.array(result)

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
    mat = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return mat

def eigenvalue(matrix):
    w, v = np.linalg.eig(matrix)
    return w

def eigenvectors(matrix):
    w, v = np.linalg.eig(matrix)
    return v

def sigmavalue(matrix):
    sigma_val = []
    eigen_val = eigenvalue(matrix)
    for val in eigen_val:
        sigma_val.append(abs(val)**(0.5))
    return np.array(sigma_val)

def sigma_matrix(matrix):
    aat = multiply(matrix, transpose(matrix))
    sigma_val = sigmavalue(aat)
    s = np.round(sigma_val, decimals=5)
    return s 

def vtrans_matrix(matrix):
    ata = multiply(transpose(matrix), matrix)
    vt = transpose(eigenvectors(ata))
    vt = np.array(vt)
    for i in range(len(vt)):
        norm = np.linalg.norm(vt[i])
        vt[i] = vt[i]/norm
    return np.round(vt, decimals=5)

def u_matrix(matrix):
    aat = multiply(matrix, transpose(matrix))
    u = eigenvectors(aat)
    u = np.array(u)
    for i in range(len(u)):
        norm = np.linalg.norm(u[i])
        u[i] = u[i]/norm
    return np.round(u, decimals=5)

def svd_matrix(matrix):
    u, sigma, vt = np.linalg.svd(matrix)
    return u, sigma, vt

def compress_matrix(matrix, rank):
    u, s, vt = svd_matrix(matrix)
    leftSide = np.matmul(u[:, 0:rank], np.diag(s)[0:rank, 0:rank])
    comp_matrix = np.matmul(leftSide, vt[0:rank, :])
    res_matrix = comp_matrix.astype('uint8')
    return res_matrix

def test_matrix(matrix, rank):
    u = u_matrix(matrix)
    s = sigma_matrix(matrix)
    vt = vtrans_matrix(matrix)
    leftSide = np.matmul(u[:, 0:rank], np.diag(s)[0:rank, 0:rank])
    comp_matrix = np.matmul(leftSide, vt[0:rank, :])
    res_matrix = comp_matrix.astype('uint8')
    return res_matrix

# matrix1 = [[3,1,1], [-1,3,1]]
# aat = multiply(matrix1, transpose(matrix1))
# ata = multiply(transpose(matrix1), matrix1)