import numpy as np

def svd_matrix(matrix):
    u, sigma, vt = np.linalg.svd(matrix)
    return u, sigma, vt

def compress_matrix(matrix, rank):
    u, s, vt = svd_matrix(matrix)
    leftSide = np.matmul(u[:, 0:rank], np.diag(s)[0:rank, 0:rank])  # Perkalian matriks u, s, vt untuk memperoleh matriks yang terkompresi
    comp_matrix = np.matmul(leftSide, vt[0:rank, :])
    res_matrix = comp_matrix.astype('uint8')
    return res_matrix

def max_rank(matrix):
    u, sigma, vt = np.linalg.svd(matrix)
    return len(sigma)

'''
BONUS UTILITY
'''

def transpose(matrix):
    return np.transpose(matrix)

def multiply(matrix1, matrix2):
    # syarat digunakan : ukuran matrix1 dan matrix2 mengikuti kaidah perkalian matriks dan menghasilkan matriks result
    return np.dot(matrix1.tolist(), matrix2.tolist())

def eigenvalue(matrix):
    w, v = np.linalg.eig(matrix)
    return w

def eigenvectors(matrix):
    w, v = np.linalg.eig(matrix)
    return v

def sigma_matrix(matrix):  
    # sigma matrix didapat dari akar dari nilai eigen matrix AAT (A*Atranspose) lalu diurut menurun
    aat = multiply(matrix, transpose(matrix))
    sigma_val = []
    eigen_val = eigenvalue(aat)
    for val in eigen_val:
        sigma_val.append(abs(val)**(0.5))
    sigma_val = np.array(sigma_val)
    return np.flip(np.sort(sigma_val)) 

def u_matrix(matrix):
    # U matrix didapat dari vektor eigen matrix AAT dimana urutan vektor eigen menyesuaikan eigenvalue yang diurut menurun
    aat = multiply(matrix, transpose(matrix))
    eigen = eigenvalue(aat)
    indexarr = np.flip(np.argsort(eigen))
    vectors = [[] for i in range(len(eigen))]
    u = transpose(eigenvectors(aat))
    for i in range(len(eigen)):
        vectors[i] = u[indexarr[i]]
    vectors = np.array(vectors)
    for i in range(len(vectors)):       # Normalisasi vektor
        norm = np.linalg.norm(vectors[i])
        vectors[i] = vectors[i].real/norm
    return transpose(vectors)

def vtrans_matrix(matrix):
    # Vt matrix didapat dari vektor eigen matrix ATA dimana urutan vektor eigen menyesuaikan eigenvalue yang diurut menurun
    ata = multiply(transpose(matrix), matrix)
    eigen = eigenvalue(ata)
    indexarr = np.flip(np.argsort(eigen))
    vectors = [[] for i in range(len(eigen))]
    vt = transpose(eigenvectors(ata))
    for i in range(len(eigen)):
        vectors[i] = vt[indexarr[i]]
    vectors = np.array(vectors)
    for i in range(len(vectors)):   # Normalisasi vektor
        norm = np.linalg.norm(vectors[i])
        vectors[i] = vectors[i].real/norm
    return vectors

def compress_matrix_manual(matrix, rank):
    u = u_matrix(matrix)
    s = sigma_matrix(matrix)
    vt = vtrans_matrix(matrix)
    leftSide = np.matmul(u[:, 0:rank], np.diag(s)[0:rank, 0:rank]) # Perkalian matriks u, s, vt untuk memperoleh matriks yang terkompresi
    comp_matrix = np.matmul(leftSide, vt[0:rank, :])
    res_matrix = comp_matrix.astype('uint8')
    return res_matrix