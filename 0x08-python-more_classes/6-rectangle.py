#!/usr/bin/python3
"""Defining a rectangle class'"""

class Rectangle:
	"""Representing a rectangle.

	Attributes:
		number_of_instances (int): The number of Rectangle instances."""

	number_of_instances = 0
	def __init__(self, width=0, height=0):
		"""Initialization of a new Reactangle.

	Args:
		width (int): The width of the initialized rectangle.
		height (int): The height of the initialized rectangle."""

	type(self).number_of_instances += 1
	self.width = width
	self.height = height

	@property
	def width(self):
		"""Get/set the width of the Rectangle."""
		return self.__width

	@width.setter
	def width(self, value):
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		if value < 0:
			raise Valueerror("width must be >= 0")
		self.__width = value
