
class Node(object):
	def __init__(self, data, parent):
		self.data = data
		self.parent = parent
		self.left = None
		self.right = None
		self.balance = 0

	def insert(self, data, parent):
		if data < self.data:
			if not self.left:
				self.left = Node(data, parent)
			else:
				self.left.insert(data, parent)
		else:
			if not self.right:
				self.right = Node(data, parent)
			else:
				self.right.insert(data, parent)
		return parent

	def travesia(self):
		if self.left:
			self.left.travesia()
		print(self.data)
		if self.right:
			self.right.travesia()

	def getMax(self):
		if not self.right:
			return self.data
		else:
			return self.right.getMax()

	def getMin(self):
		if not self.left:
			return self.data
		else:
			return self.left.getMin()