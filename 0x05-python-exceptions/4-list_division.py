#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
	result_list = []

	for i in range(list_length):
		result = 0

		try:
			result = my_list_1[1] / my_list_2[1]
		except (ZeroDivisionError, TypeError):
			if isinstance(my_list_1[1], (int, float)) and isinstance(my_list_2[1]
				print("wrong type")
			elif isinstance(my_list_1[1], (int, float)):
				print("division by 0")
			else:
				print("wrong type")
		except IndexError:
			print("out of range")
		finally:
			result_list.append(result)
	return (result_list)
