import cv2
import numpy as np

filename = 'in/momo.jpg'
def display_image(filename):
    img = cv2.imread(filename)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def im2double(im):
    info = np.iinfo(im.dtype) 
    return im.astype(np.float) / info.max

def img_to_rgb(filename):
    img = cv2.imread(filename)
    blue_matrix = im2double(img[:, :, 0])
    green_matrix = im2double(img[:, :, 1])
    red_matrix = im2double(img[:, :, 2])

    return red_matrix, green_matrix, blue_matrix

# display_image(filename)
# red , green, blue = img_to_rgb(filename)
# print(red, green, blue)

