def pascal_triangle_II_recursive(row):
	if row == 0:
		return [1]
	if row == 1:
		return [1,1]

	res = [1] * (row+1)
	pre = pascal_triangle_II(row-1)
	for i in range(1, row):
		res[i] = pre[i] + pre[i-1]

	return res

def pascal_triangle_II(row):
	if row == 0:
		return [1]

	if row == 1:
		return [1, 1]

	pre = [1, 1]
	for i in range(2, row+1):
		res = [1] * (row+1)
		for j in range(1, i):
			res[j] = pre[j] + pre[j-1]
		pre = res

	return res			