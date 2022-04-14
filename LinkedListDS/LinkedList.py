from LinkedListDS.Node import Nodo

class linked(object):
	def __init__(self):
		self.head = None
		self.counter = 0

	def traverse(self):
		actualNodo = self.head
		while actualNodo is not None:
			print("{}".format(actualNodo.dato))
			actualNodo = actualNodo.nextNodo

	def size(self):
		return self.counter()

	def insertStart(self, dato):
		self.counter += 1
		newNodo = Nodo(dato)
		if not self.head:
			self.head = newNodo
		else:
			newNodo.nextNodo = self.head
			self.head = newNodo

	def insertEnd(self, dato):
		if self.head is None:
			self.insertStart(dato)
			return
		self.counter += 1
		newNodo = Nodo(dato)
		actualNodo = self.head
		while actualNodo.nextNodo is not None:
			actualNodo = actualNodo.nextNodo
		actualNodo.nextNodo = newNodo

	def remove(self, dato):
		self.counter -= 1
		if self.head:
			if dato == self.head.dato:
				self.head = self.head.nextNodo

			else:
				self.head.remove(dato, self.head)
