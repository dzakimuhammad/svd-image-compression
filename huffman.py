from imgUtil import img_to_rgb, write_img, merge_rgb
import numpy as np
import queue
from PIL import Image

class Node:
	def __init__(self):
		self.prob = None
		self.code = None
		self.data = None
		self.left = None
		self.right = None 	# the color (the bin value) is only required in the leaves
	def __lt__(self, other):
		if (self.prob < other.prob):		# define rich comparison methods for sorting in the priority queue
			return 1
		else:
			return 0
	def __ge__(self, other):
		if (self.prob > other.prob):
			return 1
		else:
			return 0

def tree(probabilities):
	prq = queue.PriorityQueue()
	for color,probability in enumerate(probabilities):
		leaf = Node()
		leaf.data = color
		leaf.prob = probability
		prq.put(leaf)

	while (prq.qsize()>1):
		newnode = Node()		# create new node
		l = prq.get()
		r = prq.get()			# get the smalles probs in the leaves
						# remove the smallest two leaves
		newnode.left = l 		# left is smaller
		newnode.right = r
		newprob = l.prob+r.prob	# the new prob in the new node must be the sum of the other two
		newnode.prob = newprob
		prq.put(newnode)	# new node is inserted as a leaf, replacing the other two 
	return prq.get()		# return the root node - tree is complete

def huffman_traversal(root_node,tmp_array,f):		# traversal of the tree to generate codes
	if (root_node.left is not None):
		tmp_array[huffman_traversal.count] = 1
		huffman_traversal.count+=1
		huffman_traversal(root_node.left,tmp_array,f)
		huffman_traversal.count-=1
	if (root_node.right is not None):
		tmp_array[huffman_traversal.count] = 0
		huffman_traversal.count+=1
		huffman_traversal(root_node.right,tmp_array,f)
		huffman_traversal.count-=1
	else:
    	#count the number of bits for each color
		bitstream = ''.join(str(cell) for cell in tmp_array[1:huffman_traversal.count]) 
		f[root_node.data] = int(bitstream)

def getHuffmanDict(imgmat):
    hist = np.bincount(imgmat.ravel(),minlength=256)

    probabilities = hist/np.sum(hist)		# a priori probabilities from frequencies

    root_node = tree(probabilities)			# create the tree using the probs.
    tmp_array = np.ones([64],dtype=int)
    huffman_traversal.count = 0
    f = {}
    huffman_traversal(root_node,tmp_array,f)
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
            # print(encoded[i][j])
    encoded = np.array(encoded)
    return(encoded.astype('int64'))

def decodemat(mat, code):
    code = inversedict(code)
    decoded = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            decoded[i][j] = code[mat[i][j]]
            # print(encoded[i][j])
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