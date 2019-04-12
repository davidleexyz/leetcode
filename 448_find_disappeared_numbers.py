def find_disappeared_numbers(nums):
	res = []
	for i in range(len(nums)):
		while nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
			idx = nums[i] - 1
			nums[i], nums[idx] = nums[idx], nums[i]

	for i in range(len(nums)):
		if nums[i] != i + 1:
			res.append(i+1)

	return res