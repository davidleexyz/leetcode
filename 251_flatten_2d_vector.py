class Vector2D(object):
	def __init__(self, vector2d):
		self.row = 0
		self.col = 0
		self.vector = vector2d


	def next(self):
		res = self.vector[self.row][self.col]
		self.col += 1
		return res
			

	def hasNext(self):
		if self.row < len(self.vector):
			if self.col < len(self.vector[self.row]):
				return True
			else:
				if self.row == len(self.vector) - 1:
					return False
				else:
					self.row += 1
					self.col = 0
					return True
		return False
