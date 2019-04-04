def remove_duplicates_II(nums):
	if not nums:
		return 0

	if len(nums) == 1:
		return 1

	count = 1
	last = 0
	for i in range(1, len(nums)):
		if nums[i] == nums[last]:
			count += 1
			if count <= 2:
				last += 1
				nums[last] = nums[i]
		else:
			count = 1
			last += 1
			nums[last] = nums[i]

	return last + 1
			