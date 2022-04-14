from BinarySearchTreeDS.Node import Node

class BST(object):
	def __init__(self):
		self.root = None

	def insert(self, data):
		if not self.root:
			self.root = Node(data)
		else:
			self.root.insert(data)

	def remove(self, dataToRemove):
		if self.root:
			if self.root.data == dataToRemove:
				tempNode = Node(None)
				tempNode.left = self.root
				self.root.remove(dataToRemove, tempNode)
			else:
				self.root.remove(dataToRemove, None)

	def getMax(self):
		if self.root:
			return self.root.getMax()

	def getMin(self):
		if self.root:
			return self.root.getMin()

	def travel(self):
		if self.root:
			self.root.travel()
