def rotate_function_tle(A):
	if not A:
		return 0

	max_res = -float('inf')
	for i in range(len(A)):
		B = A[i:] + A[:i]
		res = 0
		for j in range(len(B)):
			res += j * B[j]
		max_res = max(max_res, res)
	return max_res


def rotate_function(A):
	if not A:
		return 0

	total = sum(A)
	N = len(A)
	res = [0] * len(A)

	res[0] = sum([i*a for i, a in enumerate(A)])

	for i in range(1, N):
		res[i] = res[i-1] - total + A[i-1] * N

	return max(res)