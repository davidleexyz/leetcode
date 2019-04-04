def find_missing_ranges(nums, lower, upper):
	if not nums:
		return [str(lower) + "->" + str(upper) if lower != upper else str(lower)]

	res = []

	if lower == nums[0]:
		start = nums[0] 
	else:
		start = lower - 1

	for i in range(0, len(nums)):
		end = nums[i]

		if end - start == 2:
			res.append(str(start+1))
		elif end - start > 2:
			res.append(str(start+1) + "->" + str(end-1))
		
		start = nums[i]

	if upper - start == 2:
		res.append(str(start+1))
	elif upper - start > 2:
		res.append(str(start+1) + "->" + str(upper))

	return res





