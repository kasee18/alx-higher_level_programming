#!/usr/bin/python3

'''defining a text file lines-counting function.'''

def write_file(filename="", text=""):
	'''write a string to a UTF-8 text file and return the number of characters written.'''
	lines = 0
	with open(filename) as f:
		for line in f:
			lines += 1
	return(count)
