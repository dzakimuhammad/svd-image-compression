# Image Compression with SVD
Tugas CaIRK 2019

Memanfaatkan algoritma Singular Value Decomposition untuk kompresi gambar

## Cara Penggunaan Program
1. Buka terminal, arahkan ke direktori tempat program disimpan yaitu pada folder 'svd-image-compression' atau nama folder tempat repository ini disimpan.
2. Jalankan perintah berikut untuk menjalankan program.
```
python main.py
```
3. Instruksi lebih lanjut disediakan dalam program

Catatan : Gambar input harus berada dalam folder 'in' dan gambar output yang dihasilkan selalu disimpan pada folder 'out'

## Penjelasan Algoritma SVD
1. Penjelasan matriks U, S, V
SVD is based on a theorem from linear algebra which says that a rectangular matrix A can
be broken down into the product of three matrices - an orthogonal matrix U, a diagonal
matrix S, and the transpose of an orthogonal matrix V

2. Pemanfaatan *rank* dalam kualitas kompresi gambar
the purpose is not to actually reconstruct the original matrix but to use the reduced dimensionality representation to identify similar words and documents.

## Referensi dan Library
### Referensi
1. https://davetang.org/file/Singular_Value_Decomposition_Tutorial.pdf
2. http://www.math.utah.edu/~goller/F15_M2270/BradyMathews_SVDImage.pdf
3. https://www.youtube.com/watch?v=SU851ljMIZ8
4. https://github.com/JoshuaEbenezer/huffman_encoding/blob/master/huffman.py
5. https://stackoverflow.com/questions/11587044/how-can-i-create-a-tree-for-huffman-encoding-and-decoding

### Library
1. Numpy : digunakan untuk pengolahan matriks (transpose, eigen, SVD, dsb.)
2. PILLOW : digunakan untuk rekonstruksi gambar
3. cv2 : digunakan untuk membaca gambar menjadi matriks yang didekomposisi menjadi matriks RGB
4. os : digunakan untuk mencari detail file berdasarkan lokasi file 
5. queue : digunakan untuk membuat priority queue dalam pembentukan pohon huffman