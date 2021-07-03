from imgUtil import img_to_rgb, compress_img, compress_img_manual, write_img, sizecompression_pct
from matrixUtil import max_rank
from time import time
from huffman import huffmancompression
import os

run = True
print("---- IMAGE COMPRESSION ----")
print()

while(run):
    invalidChoice = True 
    while(invalidChoice):
        print("Pilih opsi metode kompresi yang kamu inginkan:")
        print("1. SVD Method\n2. Huffman Code\n3. SVD Method Manual (Bonus)")
        method = int(input("Input opsi (1/2/3): "))
        if method == 1 or method == 2 or method == 3:
            invalidChoice = False
        else:
            print("Tidak ada pilihan opsi tersebut!")
        print()

    invalidChoice =True 
    while(invalidChoice):
        filename = input(("Masukkan nama file gambar pada folder in yang ingin kamu kompres (tuliskan ekstensi juga): "))
        inputfile = 'in/'+filename
        if(os.path.exists(inputfile) != True):
            print("Tidak ada file dengan nama tersebut!")
        if(not filename.lower().endswith(('.png', '.jpg', '.jpeg'))):
            print("File bukan file gambar! Pastikan nama file memiliki ekstensi '.jpg', '.jpeg', atau '.png'")
        if(os.path.exists(inputfile) == True and filename.lower().endswith(('.png', '.jpg', '.jpeg'))):
            invalidChoice = False
        print()

    invalidChoice =True 
    while(invalidChoice):
        output = input(("Masukkan nama file gambar hasil kompresi (tuliskan ekstensi juga): "))
        if(not output.lower().endswith(('.png', '.jpg', '.jpeg'))):
            print("File bukan file gambar! Pastikan nama file memiliki ekstensi '.jpg', '.jpeg', atau '.png'")
        else:
            invalidChoice = False
        print()

    outputfile = 'out/'+output
    print()

    red, green, blue = img_to_rgb(inputfile)
    maxrank = max_rank(red)

    if method == 1:
        invalidChoice =True 
        while(invalidChoice):
            rank = int(input("Masukkan nominal singular value/rank (max " +str(maxrank)+  "): "))
            if rank <= maxrank and rank > 0:
                invalidChoice = False
        print()
        start = time()
        const_matrix = compress_img(inputfile, rank)
        write_img(const_matrix, output)
        exectime = time() - start

    if method == 2:
        start = time()
        huffmancompression(inputfile, output)
        exectime = time() - start
    
    if method == 3:
        invalidChoice =True 
        while(invalidChoice):
            rank = int(input("Masukkan nominal singular value/rank (max " +str(maxrank)+  "): "))
            if rank <= maxrank and rank > 0:
                invalidChoice = False
        print()
        start = time()
        const_matrix = compress_img_manual(inputfile, rank)
        write_img(const_matrix, output)
        exectime = time() - start

    print("Kompresi gambar berhasil! Gambar berhasil tersimpan pada " + outputfile + "!")
    print("Waktu eksekusi program: " + str(round(exectime, 3)) + " detik")
    print("Persentase ukuran memori gambar yang dikompresi terhadap gambar original: " + str(round(sizecompression_pct(inputfile, outputfile), 2)) + "%")
    print()
    end = input("Apakah Anda ingin menggunakan program ini kembali (y/n)? ")
    if end == "n":
        run = False