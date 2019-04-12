def find_unsorted_subarray_tle(nums):
	start_idx = 0
	while start_idx < len(nums):
		start = nums[start_idx]
		flag = True
		for j in range(start_idx+1, len(nums)):
			if start <= nums[j]:
				continue
			else:
				flag = False
				break

		if flag == True:
			start_idx += 1
		else:
			break

	end_idx = len(nums) - 1
	while end_idx > 0:
		end = nums[end_idx]
		flag = True
		for j in range(end_idx-1, -1, -1):
			if end >= nums[j]:
				continue
			else:
				flag = False
				break
		if flag == True
			end_idx -= 1
		else:
			break

	return max(end_idx - start_idx + 1, 0)


def find_unsorted_subarray(nums):
	if not nums or len(nums) == 1:
		return 0
	
	sorted_nums = sorted(nums)
	for i in range(len(nums)):
		if nums[i] != sorted_nums[i]:
			break

	start = i

	for i in reversed(range(len(nums))):
		if nums[i] != sorted_nums[i]:
			break

	end = i

	return max(end - start + 1, 0)


