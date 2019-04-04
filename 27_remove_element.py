def remove_element(nums, val):
	if not nums:
		return 0

	last = -1
	for num in nums:
		if num != val:
			last += 1
			nums[last] = num
	return last + 1