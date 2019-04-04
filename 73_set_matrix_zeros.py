# use mark-sweep method
def set_matrix_zero(matrix):
	m = len(matrix)
	n = len(matrix[0])
	inf = float('inf')
	for i in range(m):
		for j in range(n):
			if matrix[i][j] == inf:
				continue
			if matrix[i][j] == 0:
				for col in range(n):
					if col != j and matrix[i][col] != 0:
						matrix[i][col] = inf
				for row in range(m):
					if row != i and matrix[row][j] != 0:
						matrix[row][j] = inf

	for i in range(m):
		for j in range(n):
			if matrix[i][j] == inf:
				matrix[i][j] = 0
