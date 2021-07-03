import cv2
import os
from PIL import Image
from matrixUtil import compress_matrix, compress_matrix_manual

def img_to_rgb(filename):       # Pemecahan gambar dengan path relatif 'filename' menjadi matriks RGB
    img = cv2.imread(filename)
    blue_matrix = img[:, :, 0]
    green_matrix = img[:, :, 1]
    red_matrix = img[:, :, 2]

    return red_matrix, green_matrix, blue_matrix

def compress_img(filename, rank):   # Proses kompresi gambar lalu menggabungkannya kembali menjadi satu matriks gambar yang dapat ditulis
    # Filename : path relatif gambar, rank : rank matriks yang digunakan dalam proses rekonstruksi matriks
    red, green, blue = img_to_rgb(filename)
    comp_red = Image.fromarray(compress_matrix(red, rank))
    comp_green = Image.fromarray(compress_matrix(green, rank))
    comp_blue = Image.fromarray(compress_matrix(blue, rank))
    return Image.merge("RGB",(comp_red, comp_green, comp_blue))

def write_img(image, filename):    # Menuliskan matriks gambar 'image' menjadi gambar dengan nama file 'filename' pada folder 'out'
    path = 'out/'+filename
    image.save(path)

def get_imgsize(imgpath):   # Mengembalikan ukuran file 'imgpath'
    return os.path.getsize(imgpath)

def sizecompression_pct(original_path, compressed_path):    # Mengembalikan persentase ukuran file 'compressed_path' dibanding 'original_path'
    return 100*get_imgsize(compressed_path)/get_imgsize(original_path)

'''
BONUS UTILITY
'''
def compress_img_manual(filename, rank): # Proses kompresi gambar lalu menggabungkannya kembali menjadi satu matriks gambar yang dapat ditulis
    red, green, blue = img_to_rgb(filename)
    comp_red = Image.fromarray(compress_matrix_manual(red, rank))
    comp_green = Image.fromarray(compress_matrix_manual(green, rank))
    comp_blue = Image.fromarray(compress_matrix_manual(blue, rank))
    return Image.merge("RGB",(comp_red, comp_green, comp_blue))

def merge_rgb(red, green, blue):    # Proses menggabungkan matriks RGB menjadi satu matriks gambar yang dapat ditulis (Bonus Huffman Coding)
    comp_red = Image.fromarray(red).convert('L')
    comp_green = Image.fromarray(green).convert('L')
    comp_blue = Image.fromarray(blue).convert('L')
    return Image.merge("RGB",(comp_red, comp_green, comp_blue))

