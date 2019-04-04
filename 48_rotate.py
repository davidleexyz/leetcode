# transpose then reversed every row
def rotate(matrix):
	for i in range(len(matrix)):
		for j in range(i):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

	for row in matrix:
		row[:] = row[::-1]


# use python zip(*) unpack
def rotate(matrix):
	matrix[:] = zip(*matrix[::-1])
