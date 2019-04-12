def array_nesting(nums):
	visited = set()
	max_len = 0
	for num in nums:
		if num in visited:
			continue

		start, nxt = num, nums[num]
		length = 1
		while nxt != start:
			length += 1
			nxt = nums[nxt]
			visited.add(nxt)
		max_len = max(max_len, length)

	return max_len
