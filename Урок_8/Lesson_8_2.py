#  Закодируйте любую строку по алгоритму Хаффмана.

import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
	# объявление класса для хранения информации о структуре дерева
	def walk(self, code, acc):
		self.left.walk(code, acc + "0")
		self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
	# объявление класса для «листьев дерева», у них нет потомков, но есть значение символа
	def walk(self, code, acc):
		code[self.char] = acc or "0"


def huffman_code(a):
	# функция кодирования символов в коды Хаффмана
	h = []
	for i, j in Counter(a).items():
		h.append((j, len(h), Leaf(i)))
	heapq.heapify(h)
	count = len(h)
	while len(h) > 1:
		i1, _count1, left = heapq.heappop(h)
		i2, _count1, right = heapq.heappop(h)
		heapq.heappush(h, (i1 + i2, count, Node(left, right)))
		count += 1
	code = {}
	if h:
		[(_freq, _count, root)] = h
		root.walk(code, "")
	return code


def huffman_decode(encoded, code):
	# функция декодирования исходной строки по кодам Хаффмана
	x = []
	enc_ch = ""
	for i in encoded:
		enc_ch += i
		for j in code:
			if code.get(j) == enc_ch:
				x.append(j)
				enc_ch = ""
				break
	return "".join(x)


array = input('Введите строку :\n')
code = huffman_code(array)
encoded = "".join(code[i] for i in array)
for i in sorted(code):
	print("{}: {}".format(i, code[i]))
print(encoded)
print(huffman_decode(encoded, code))
