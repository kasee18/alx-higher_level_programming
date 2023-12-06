#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
	only_different_set = set()
	for element in set_1:
		if element not in set_2:
			only_different_set.add(element)
	for element in set_2:
		if element not in set_1:
			only_different_set.add(element)
	return only_different_set
