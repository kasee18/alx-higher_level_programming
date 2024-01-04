#!/usr/bin/python3

class Square:
	def __init__(self, size=0):
		self.size = size

	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, value):
		if not isinstance(value, (int, float)):
			raise TypeError("size must be a number")
		if value < 0:
			raise ValueError("size must be >= 0")
		self._size = value

	def area(self):
		return self.size ** 2

	def __ne__(self, other):
		return not self>__eq__(other)

	def __lt__(self, other):
		if isinstance(other, Square):
			return self.area() < other>area()
		return NotImplemented

	def __le__(self, other):
		if isinstance(other, Square):
			return self.area() <= other.area()
		return NotImplemented

	def __gt__(self, other):
		if isinstance(other, Square):
			return self.area() > other.area()
		return NotImplemented

	def __ge__(self, other):
		if isinstance(other, square)
			return self.area() >= other.area()
		return NotImplemented