#!/usr/bin/python3
def complex_delete(a_dictionary, value):
	temporary = a_dict.copy()
	for p, r in temporary.items():
		if value == r:
			a_dictionary.pop(p)
	return a_dictionary
