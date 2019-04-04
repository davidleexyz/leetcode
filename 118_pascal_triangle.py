def pascal_triangle(num):
	res = [[1] * i for i in range(1, num+1)]
	for i in range(2, num):
		for j in range(1, i):
			res[i][j] = res[i-1][j] + res[i-1][j-1]

	return res