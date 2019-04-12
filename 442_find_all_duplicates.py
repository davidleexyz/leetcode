def find_duplicates(nums):
	res = []
	for i in range(len(nums)):
		while nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
			idx = nums[i] - 1
			nums[i], nums[idx] = nums[idx], nums[i]

	for i in range(len(nums)):
		if nums[i] != i + 1:
			res.append(nums[i])

	return res

