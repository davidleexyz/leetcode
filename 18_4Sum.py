# find integers a,b,c,d in nums, that a+b+c+d = target
def four_sum(nums, target):
	nums.sort()
	result = []
	for i in range(len(nums)):
		if i > 0 and nums[i] == nums[i-1]:
			continue
		for j in range(i+1, len(nums)):
			if j > i+1 and nums[j] == nums[j-1]:
				continue
			l, r = j+1, len(nums)-1
			while l < r:
				tmp = nums[i] + nums[j] + nums[l] + nums[r]
				if tmp == target:
					result.append([nums[i], nums[j], nums[l], nums[r]])
					while l < r and nums[l+1] == nums[l]:
						l += 1
					while l < r and nums[r-1] == nums[r]:
						r -= 1
					l += 1
					r -= 1
				elif tmp < target:
					while l < r and nums[l] == nums[l+1]:
						l += 1
					l += 1
				else:
					while l < r and nums[r-1] == nums[r]:
						r -= 1
					r -= 1
	return result


