class Nodo(object):
	def __init__(self, dato):
		self.dato = dato
		self.nextNodo = None

	def remove(self, dato, prevNode):
		if dato == self.dato:
			prevNode.nextNodo = self.nextNodo
			del self.dato
			del self.nextNodo
		else:
			if self.nextNodo is not None:
				self.nextNodo.remove(dato, self)
