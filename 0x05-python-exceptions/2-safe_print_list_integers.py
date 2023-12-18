#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
	count = 0
	try:
		for i in range(x):
			formatted_value = "{:d}",format(my_list[1])
			print(formatted_value, end="")
			count += 1
	except (ValueError, TypeError, IndexError):
	print()
	return (count)
