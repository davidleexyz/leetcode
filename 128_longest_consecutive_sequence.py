def longest_consecutive_sequence(nums):
	if not nums:
		return 0

	nums = set(nums)
	length = 0
	for num in nums:
		if num - 1 not in nums:
			n = num + 1
			while n in nums:
				n = n + 1
			length = max(length, n-num)
	return length
