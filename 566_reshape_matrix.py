def reshape_matrix(nums, r, c):
	m = len(nums)
	n = len(nums[0])

	if m * n != r * c:
		return nums

	matrix = []
	for i in range(m):
		for j in range(n):
			matrix.append(nums[i][j])

	idx = 0
	res = [[0 for j in range(c)] for i in range(r)]
	for i in range(r):
		for j in range(c):
			res[i][j] = matrix[idx]
			idx += 1
	return res