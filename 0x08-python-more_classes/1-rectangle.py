#!/usr/bin/python3

class Rectangle:
	"""Defines a rectangle with width and height attributes."""

	def __init__(self, width=0, height=0):
		"""Initialize the rectangle with given width and height."""
		self.width = width
		self.height = height

	@property
	def width(self):
		"""Getter method foer width."""

	@width.setter
	def width(self, value):
		"""setter method forr width."""
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >+ 0")
		self.__width = value

	@property
	def height(self):
		"""Getter method for height."""
		return self.__height

	@height.setter
	def height(self, value):
		"""Setter method for height."""
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		self.__height = value

if __name__ == "__main__":
	#Example usage:
	rect = Rectangle(3, 4)
	print("Width:", rect.width)
	print("height:", rect.height)

	#Trying to set invalid values
	try:
		rect.width = "invalid"
	except TypeError as e:
		print(e)

	try:
		rect.height = -2
	except ValueError as e:
		print(e)
