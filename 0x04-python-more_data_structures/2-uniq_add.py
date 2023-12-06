#!usr/bin/python3
def uniq_add(my_list=[]):
	unique_set = set ()
	for number in my list:
		if isinstance(number, int): #check if the number is integer
			unique_set.add(number)
	result = sum(unique_set)
	return result

