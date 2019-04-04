def find_celebrity(n):
	candidate = -1
	for i in range(n):
		j = 0
		while j < n:
			if j != i:
				if knows(i,j):
					break
				else:
					j += 1
		if j != i and j == n:
			candidate = i
			break

	if candidate != -1:
		i = 0
		while i < n:
			if i == candidate:
				i += 1
				continue
			
			if knows(i, candidate):
				i += 1
			else:
				return -1

	return candidate



