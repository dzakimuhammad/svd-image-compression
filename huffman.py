from imgUtil import img_to_rgb, write_img, merge_rgb
import numpy as np
import queue

class Node:
	def __init__(self):
		self.prob = None  # peluang kemunculan data dalam matriks
		self.huff = ''	# kode arah pohon huffman (0/1)
		self.data = None	# data atau elemen 
		self.left = None
		self.right = None 	
	def __lt__(self, other):	# definisi operasi perbandingan (kurang dari)
		if (self.prob < other.prob):
			return 1
		else:
			return 0
	def __ge__(self, other):	# definisi operasi perbandingan (lebih dari sama dengan)
		if (self.prob > other.prob):
			return 1
		else:
			return 0

def create_tree(probabilities):
	prq = queue.PriorityQueue()		# inisialisasi prio queue
	for colorint, probability in enumerate(probabilities):
		leaf = Node()
		leaf.data = colorint
		leaf.prob = probability
		prq.put(leaf)

	while (prq.qsize()>1):
		newnode = Node()		# inisialisasi node baru
		l = prq.get()
		r = prq.get()			# menggabungkan 2 node dengan prob terkecil

		l.huff = 0
		r.huff = 1

		newnode.left = l
		newnode.right = r
		newprob = l.prob+r.prob		# prob node baru adalah jumlah prob 2 node dengan prob terkecil
		newnode.prob = newprob
		prq.put(newnode)

	return prq.get()

def traverseNodes(node, val='', f={}):
    # kode huffman untuk node yang diperiksa
    newVal = val + str(node.huff)
 
    # jika node bukan daun maka periksa node anaknya
    if(node.left is not None):
        traverseNodes(node.left, newVal, f)
    if(node.right is not None):
        traverseNodes(node.right, newVal, f)
 
    else:	# jika node adalah daun, assign kode huffman newVal dalam dictionary dengan key data
        f[node.data] = newVal

def getHuffmanDict(imgmat):		# Fungsi mengembalikan dictionary yang menghubungkan elemen-elemen pada matriks gambar dengan kode huffmannya 
	hist = np.bincount(imgmat.ravel(), minlength=256)	# membentuk array frekuensi sesuai indeks

	probabilities = hist/np.sum(hist)		# array peluang setiap data

	root_node = create_tree(probabilities)			# membuat pohon huffman berdasarkan array peluang yang telah dibentuk
	f = {}
	traverseNodes(root_node, '', f)	# membentuk dictionary kode huffman yang disimmpan dalam f
	return f

def inversedict(dictionary):
    inv = {v: k for k, v in dictionary.items()}
    return inv

def encodemat(mat, code):
    encoded = [['  ' for j in range(len(mat[0]))] for i in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            a = str(code[mat[i][j]])
            encoded[i][j] = a
    encoded = np.array(encoded)
    return encoded

def decodemat(mat, code):
	code = inversedict(code)
	decoded = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			decoded[i][j] = code[str(mat[i][j])]
	decoded = np.array(decoded)
	return(decoded)

def huffmancompression(input, output):
	red, green, blue = img_to_rgb(input)

	encoded_red = encodemat(red, getHuffmanDict(red))
	encoded_green = encodemat(green, getHuffmanDict(green))
	encoded_blue = encodemat(blue, getHuffmanDict(blue))

	decoded_red = decodemat(encoded_red, getHuffmanDict(red))
	decoded_green = decodemat(encoded_green, getHuffmanDict(green))
	decoded_blue = decodemat(encoded_blue, getHuffmanDict(blue))
	
	img = merge_rgb(decoded_red, decoded_green, decoded_blue)
	write_img(img, output)

# filename = 'in/momo.jpg'
# huffmancompression(filename, 'momo.jpg')
# red, green, blue = img_to_rgb(filename)
# a = getHuffmanDict(red)
# b = testHuffmanDict(red)
# print(len(a))
# print(len(b))

