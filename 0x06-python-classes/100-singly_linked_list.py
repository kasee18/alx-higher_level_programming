#!/usr/bin/python3
"""Class definition for singly-linked list."""

class Node:
	"""Representation of a node in a singly-linked list."""

	def__init__(self, data, next_node=None):
		 """Initialization of a new Node.

		Args:
			data (int): The data of the new Node."""

		self.data = data
		self.next_node = next_node

	@property
	def data(self):
		"""Get/set the data of the Node."""
		return (self.__data)

	@data.setter
	def data(self, value):
		if not isinstance(value, int):
			raise TypeError("data must be an integer")
		self.__data = value

	@property
	def next_node(self):
		"""get/set the next_node of the Node."""
		return (self.__next_node)

	@next_node.setter
	def next_node(self, value):
		if not isinstance(value, Node) and value os not None:
			raise TypeError("next_node must be a Node object")
		self.__next_node = value

	class singlyLinkedList:
		"""Reprssenting singly linked list."""

		def __init__(self):
			self.head = None

		def sorted_insert(self, value):
			"""for sorting inserted values"""
			new_node = Node(value)

			if self.head is None or self.head.data > value:
				new_node.next_none = self.head
				"""head initialization in the function"""
				self.head = new_node
			else:
				current = self.head
				"""current representation/initialization"""
				while current.next_node is non None and current.next_node.data < value:
					current = current.next_node
		def__str__(self):
			result = []
			current = self.head
			while current:
				result.append(str(current.data))
				current = current.next_node
			return '\n'.join(result)
