# -*- coding: utf-8 -*-

def createVectorNamesFromFile(filename):
	'''
	This function, given a specific file path, given it is a txt, will extract every rows and will create a list in which each element is a row without the flags \n

	INPUT
	- filename: that is just the filepath, it is expected to be a txt

	OUTPUT
	- output_vec: a list, in which each element is a line of the file without new line flags \n
	'''

	output_vec = []
	with open(filename) as f:
		lines = f.readlines()
		for line in lines:
			output_vec.append(line.replace('\n', ''))

	return output_vec


if __name__ == '__main__':
	print createVectorNamesFromFile('laqab_M.txt')
	print createVectorNamesFromFile('laqab_F.txt')
	print createVectorNamesFromFile('nisbah_M.txt')