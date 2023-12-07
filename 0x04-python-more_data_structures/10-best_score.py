#!/usr/bin/python3
def best_score(a_dictionary):
	if not a_dictionary:
		return None
	Max = 0
	for key, numbers in a_dictionary.items():
		if numbers > Max:
			Max = numbers
	for key, numbers in a_dictionary.items():
		if numbers == Max:
			return key
