def sprial_matrix_II(n):
	elements = [x for x in range(1, n*n+1)]
	min_left, min_up = 0, 0
	max_right, max_down = n-1, n-1
	direction = 0
	current = 0
	matrix = [[0] * n for i in range(n)]
	while min_left <= max_right and min_up <= max_down:
		if direction == 0:
			for i in range(min_left, max_right+1):
				matrix[min_up][i] = elements[current]
				current += 1
				if current >= len(elements):
					return matrix
			direction = 1
		elif direction == 1:
			for i in range(min_up+1, max_down+1):
				matrix[i][max_right] = elements[current]
				current +=1 
				if current >= len(elements):
					return matrix
			direction = 2
		elif direction == 2:
			for i in range(max_right-1, min_left-1, -1):
				matrix[max_down][i] = elements[current]
				current += 1
				if current >= len(elements):
					return matrix
			direction = 3
		else:
			for i in range(max_down-1, min_up, -1):
				matrix[i][min_left] = elements[current]
				current += 1
				if current >= len(elements):
					return matrix
			direction = 0
			min_left += 1
			min_up += 1
			max_right -= 1
			max_down -= 1