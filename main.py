from imgUtil import compress_img, write_img, sizecompression_pct
from time import time
# from matrixUtil import 

print("---- IMAGE COMPRESSION ----")
print()

print("Pilih opsi metode kompresi yang kamu inginkan:")
print("1. SVD Method\n2. Huffman Code\n")
method = int(input("Input opsi (1/2): "))
print()

filename = input(("Masukkan nama file gambar pada folder in yang ingin kamu kompres (tuliskan ekstensi juga): "))
inputfile = 'in/'+filename
print()
output = 'out/'+filename

rank = int(input("Masukkan nominal singular value/rank : "))
print()

start = time()
if method == 1:
    const_matrix = compress_img(inputfile, rank)
    write_img(const_matrix, filename)
    exectime = time() - start
    print("Kompresi gambar berhasil!")
    print("Waktu eksekusi program: " + str(round(exectime, 3)) + " detik")
    print("Persentase ukuran memori gambar yang dikompresi terhadap gambar original: " + str(round(sizecompression_pct(inputfile, output), 2)) + "%")

else:
    end = time()
    print