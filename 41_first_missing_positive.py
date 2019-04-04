def first_missing_positive(nums):
	for i in range(len(nums)):
		while nums[i] >= 0 and nums[i] < len(nums) and nums[nums[i] - 1] != nums[i]:
			index = nums[i] - 1
			nums[index], nums[i] = nums[i], nums[index]

	for i in range(len(nums)):
		if nums[i] != i + 1:
			return i+1

	return len(nums) + 1