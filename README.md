# Image Compression with SVD
Tugas CaIRK 2019

Memanfaatkan algoritma Singular Value Decomposition untuk kompresi gambar

## Identitas Pembuat:
1. Dzaki Muhammad 13519049

## Struktur Direktori:
1. **folder in** -> lokasi penyimpanan gambar untuk keperluan input program.
2. **folder out** -> lokasi penyimpanan gambar sebagai output program.
3. **matrixUtil.py** -> file python berisi fungsi beserta prosedur yang berguna dalam pengolahan matriks dan pembentukan matriks algoritma SVD
4. **imgUtil.py** -> file python berisi fungsi beserta prosedur yang berguna dalam pengolahan gambar termasuk dekomposisi dan kompresi gambar
5. **huffman.py** -> file python berisi fungsi beserta prosedur implementasi *huffman coding* dalam kompresi gambar
6. **main.py** -> file program utama

## Cara Penggunaan Program
1. Buka terminal, arahkan ke direktori tempat program disimpan yaitu pada folder 'svd-image-compression' atau nama folder tempat repository ini disimpan.
2. Jalankan perintah berikut untuk menjalankan program.
```
python main.py
```
3. Instruksi lebih lanjut disediakan dalam program

Catatan : Gambar input harus berada dalam folder 'in' dan gambar output yang dihasilkan selalu disimpan pada folder 'out'

## Penjelasan Algoritma 
Algoritma SVD didasarkan pada teorema dalam aljabar linier yang menyatakan bahwa sebuah matrix A 2D dapat dipecah menjadi hasil perkalian dari 3 sub-matriks - matriks ortogonal U, matriks diagonal S, dan transpose dari matriks ortogonal V. Dekomposisi matriks ini dapat dinyatakan sesuai persamaan berikut. 

<div align="center">

![a=usv](https://latex.codecogs.com/png.latex?%5Cdpi%7B120%7D%20%5CLARGE%20A_%7Bm%5Ctimes%20n%7D%20%3D%20U_%7Bm%5Ctimes%20m%7D%5C%20S_%7Bm%20%5Ctimes%20n%7D%5C%20V_%7Bnxn%7D%5E%7BT%7D)

</div>

1. Penjelasan matriks U, S, V
* Matriks U adalah matriks yang kolomnya terdiri dari vektor eigen ortonormal dari matriks AA<sup>T</sup>. Matriks ini menyimpan informasi yang penting terkait baris-baris matriks awal, dengan informasi terpenting disimpan di dalam kolom pertama.
* Matriks S adalah matriks diagonal yang berisi akar dari nilai eigen matriks U atau V yang terurut menurun.
* Matriks V adalah matriks yang kolomnya terdiri dari vektor eigen ortonormal dari matriks A<sup>T</sup>A. Matriks ini menyimpan informasi yang penting terkait kolom-kolom matriks awal, dengan informasi terpenting disimpan dalam baris pertama.

2. Pemanfaatan *rank* dalam kualitas kompresi gambar
Rank dalam SVD adalah jumlah dari singular value yang bukan nol dari suatu matriks. Rank memiliki nilai maksimal sebesar jumlah baris/kolom dari matriks S. Seperti yang telah dijelaskan informasi-informasi yang disimpan dalam matriks U, S, V diurutkan dari informasi yang terpenting hingga informasi yang insignifikan. Sehingga jumlah singular value yang digunakan dalam rekonstruksi matriks gambar berpengaruh dalam keakuratan hasil matriks yang direkonstruksi. Semakin banyak jumlah singular value/rank (semakin banyak informasi penting), semakin akurat gambar luaran yang dihasilkan. 

## Referensi dan Library
### Referensi
1. https://davetang.org/file/Singular_Value_Decomposition_Tutorial.pdf
2. http://www.math.utah.edu/~goller/F15_M2270/BradyMathews_SVDImage.pdf
3. http://pillowlab.princeton.edu/teaching/statneuro2018/slides/notes03a_SVDandLinSys.pdf
4. https://www.youtube.com/watch?v=SU851ljMIZ8
5. https://github.com/JoshuaEbenezer/huffman_encoding/blob/master/huffman.py
6. https://stackoverflow.com/questions/11587044/how-can-i-create-a-tree-for-huffman-encoding-and-decoding

### Library
1. Numpy : digunakan untuk pengolahan matriks (transpose, eigen, SVD, dsb.)
2. PILLOW : digunakan untuk rekonstruksi gambar
3. cv2 : digunakan untuk membaca gambar menjadi matriks yang didekomposisi menjadi matriks RGB
4. os : digunakan untuk mencari detail file berdasarkan lokasi file 
5. queue : digunakan untuk membuat priority queue dalam pembentukan pohon huffman
6. time : digunakan untuk menghitung waktu eksekusi program 