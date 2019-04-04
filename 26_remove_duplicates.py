# remove the duplicates in array in-place, and return array length
def remove_duplicates(nums):
	if not nums:
		return 0
	
	last = 0
	# keep last cursor point to the new array last element
	for i in range(len(nums)):
		if nums[last] != nums[i]:
			last += 1
			nums[last] = nums[i]
	return last + 1
