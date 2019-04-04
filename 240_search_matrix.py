def search_matrix(matrix, target):
	if not matrix:
		return False
	
	row, col = 0, len(matrix[0]) - 1
	while row < len(matrix) and col >= 0:
		if target < matrix[row][col]:
			col -= 1
		elif target >  matrix[row][col]:
			row += 1
		else:
			return True
	return False


