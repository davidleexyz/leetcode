def summary_ranges(nums):
	lookup = {}
	for num in nums:
		lookup[num] = 1

	res = []
	i = 0
	while i < len(nums):
		start = nums[i]
		end = start	
		while end in lookup:
			end += 1
			i += 1

		end -= 1
		if start != end:
			res.append(str(start) + '->' + str(end))
		else:
			res.append(str(start))

	return res
