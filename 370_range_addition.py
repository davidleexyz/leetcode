def range_addition(length, updates):
	res = [0] * length

	for update in updates:
		start, end, inc = update
		res[start] += inc
		res[end+1] -= inc

	for i in range(1, len(res)):
		res[i] += res[i-1]

	return res