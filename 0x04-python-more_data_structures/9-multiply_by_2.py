#!usr/bin/python3
def multiply_by_2(a_dictionary):
	new_dict = {}
	for key, numbers in a_dictionary.items():
		new_dict[key] = numbers * 2 #multiplies values by two
	return new_dict
