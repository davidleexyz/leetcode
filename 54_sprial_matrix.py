# 控制遍历的方向可以用一个 direction 的变量来实现
# direction = 0, 1, 2, 3
def spiral_matrix(matrix):
	if not matrix:
		return []

	max_right = len(matrix[0]) -1
	max_down = len(matrix) - 1
	size = len(maxtrix) * len(matrix[0])
	min_left = 0
	min_up = 0
	direction = 0
	res = []
	while min_left <= max_right and min_up <= max_down:
		if direction == 0:
			for i in range(min_left, max_right+1):
				res.append(matrix[min_up][i])
			direction = 1
			if len(res) == size:
				break
		elif direction == 1:
			for i in range(min_up+1, max_down+1):
				res.append(matrix[i][max_right])
			direction = 2
			if len(res) == size:
				break
		elif direction == 2:
			for i in range(max_right-1, min_left-1, -1):
				res.append(matrix[max_down][i])
			direction = 3
			if len(res) == size:
				break
		else:
			for i in range(max_down-1, min_up, -1):
				res.append(matrix[i][min_left])
			if len(res) == size:
				break
			direction = 0
			min_left += 1
			min_up += 1
			max_right -= 1
			max_down -= 1

	return res


