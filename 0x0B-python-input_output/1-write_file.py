#!/usr/bin/python3

'''defining a text file lines-counting function.'''

def write_file(filename="", text=""):
	'''write a string to a UTF-8 text file and return the number of characters written.'''
	with open(filename, 'w', encoding="utf-8" as file:
		count = file.write(text)
	return(count)
