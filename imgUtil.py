import cv2
import numpy as np
import os
from PIL import Image
# from matrixUtil import compress_matrix, test_matrix

filename = 'in/momo.jpg'

def img_to_rgb(filename):
    img = cv2.imread(filename)
    blue_matrix = img[:, :, 0]
    green_matrix = img[:, :, 1]
    red_matrix = img[:, :, 2]

    return red_matrix, green_matrix, blue_matrix

# def compress_img(filename, rank):
#     red, green, blue = img_to_rgb(filename)
#     comp_red = Image.fromarray(compress_matrix(red, rank))
#     comp_green = Image.fromarray(compress_matrix(green, rank))
#     comp_blue = Image.fromarray(compress_matrix(blue, rank))
#     return Image.merge("RGB",(comp_red, comp_green, comp_blue))

def compress_img(filename, rank):
    red, green, blue = img_to_rgb(filename)
    comp_red = Image.fromarray(test_matrix(red, rank))
    print(comp_red)
    comp_green = Image.fromarray(test_matrix(green, rank))
    comp_blue = Image.fromarray(test_matrix(blue, rank))
    return Image.merge("RGB",(comp_red, comp_green, comp_blue))

def merge_rgb(red, green, blue):
    comp_red = Image.fromarray(red).convert('L')
    comp_green = Image.fromarray(green).convert('L')
    comp_blue = Image.fromarray(blue).convert('L')
    return Image.merge("RGB",(comp_red, comp_green, comp_blue))

def write_img(image, filename):
    path = 'out/'+filename
    image.save(path)

def get_imgsize(imgpath):
    return os.path.getsize(imgpath)

def sizecompression_pct(original_path, compressed_path):
    return 100*get_imgsize(compressed_path)/get_imgsize(original_path)

# display_image(filename)

# const_matrix = compress_img(filename, 10)
# write_img(const_matrix, 'momo.jpg')
# print(sizecompression_pct(filename, "out/momo.jpg"))
# red, green, blue = img_to_rgb(filename)
# print(red)


