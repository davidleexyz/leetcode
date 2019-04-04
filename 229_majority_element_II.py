def majority_element_II(nums):
	if not nums:
		return []
	
	k = len(nums) // 3
	count1, count2, candidate1, candidate2 = 0, 0, nums[0], nums[0]
	for num in nums:
		if num == candidate1:
			count1 += 1
			continue
		if num == candidate2:
			count2 += 1
			continue

		if count1 == 0:
			candidate1 = num
			count1 = 1
			continue

		if count2 == 0:
			candidate2 = num
			count2 = 1
			continue

		count1 -= 1
		count2 -= 1

	count1 = 0
	count2 = 0
	for num in nums:
		if num == candidate1:
			count1 += 1
			continue

		if num == candidate2:
			count2 += 1
			continue

	res = []
	if count1 > k:
		res.append(candidate1)

	if count2 > k:
		res.append(candidate2)

	return res




