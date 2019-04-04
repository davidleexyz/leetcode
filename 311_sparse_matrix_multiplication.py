def sparse_matrix_multiplication(A, B):
	res = [[0] * len(B[0]) for i in range(len(A))]

	idxA = []
	for row in range(len(A)):
		colA = []
		for col in range(len(A[0])):
			if A[row][col] != 0:
				colA.append(col)
		idxA.append(colA)

	for i in range(len(idxA)):
		for col in idxA[i]:
			for j in range(len(B[0])): 
				res[i][j] += A[i][col] * B[col][j]

	return res
		
