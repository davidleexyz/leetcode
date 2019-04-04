def majority_element_tle(nums):
	flag = 1
	while len(nums) > 1 and flag:
		flag = 0
		for i in range(len(nums) - 1):
			if nums[i] != nums[i+1]:
				del nums[i]
				del nums[i]
				flag = 1
				break

	return nums[0]

def majority_element(nums):
	count = 0
	candidate = None
	for num in nums:
		if count == 0:
			candidate = num
		count = count + 1 if candidate == num else count - 1
	return candidate

