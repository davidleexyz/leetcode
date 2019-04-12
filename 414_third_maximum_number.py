def third_max(nums):
	if len(nums) < 3:
		return max(nums)

	small, middle, large = -float('inf'), -float('inf'), -float('inf')
	for num in nums:
		if num <= small or num == middle or num == large:
			continue
		
		if num < middle:
			small = num
		elif num < large:
			small = middle
			middle = num
		elif num > large:
			small = middle
			middle = large
			large = num

	if small != -float('inf'):
		return small
	else:
		return large
			