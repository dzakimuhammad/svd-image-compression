from imgUtil import compress_img, write_img, sizecompression_pct
from time import time
from huffman import huffmancompression
# from matrixUtil import 

print("---- IMAGE COMPRESSION ----")
print()

print("Pilih opsi metode kompresi yang kamu inginkan:")
print("1. SVD Method\n2. Huffman Code\n")
method = int(input("Input opsi (1/2): "))
print()

filename = input(("Masukkan nama file gambar pada folder in yang ingin kamu kompres (tuliskan ekstensi juga): "))
inputfile = 'in/'+filename
output = input(("Masukkan nama file gambar hasil kompresi (tuliskan ekstensi juga): "))
outputfile = 'out/'+filename

if method == 1:
    rank = int(input("Masukkan nominal singular value/rank : "))
    print()
    start = time()
    const_matrix = compress_img(inputfile, rank)
    write_img(const_matrix, output)
    exectime = time() - start

else:
    start = time()
    huffmancompression(inputfile, output)
    exectime = time() - start

print("Kompresi gambar berhasil!")
print("Waktu eksekusi program: " + str(round(exectime, 3)) + " detik")
print("Persentase ukuran memori gambar yang dikompresi terhadap gambar original: " + str(round(sizecompression_pct(inputfile, outputfile), 2)) + "%")