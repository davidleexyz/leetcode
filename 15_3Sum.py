# find integers  a, b, c in nums, that a+b+c=0

def three_sum(nums):
	nums.sort()
	res = []
	for i in range(len(nums)):
		if i > 0 and nums[i-1] == nums[i]:
			continue
		l, r = i+1, len(nums)-1
		while l < r:
			tmp = nums[i] + nums[l] + nums[r]
			if tmp == 0:
				res.append([nums[i], nums[l], nums[r]])
				while l < r and nums[l+1] == nums[l]:
					l += 1
				
				while l < r and nums[r-1] == nums[r]:
					r -= 1
				
				l += 1
				r -= 1
			elif tmp > 0:
				while l < r and nums[r-1] == nums[r]:
					r -= 1
				r -= 1
			else:
				while l < r and nums[l+1] == nums[l]:
					l += 1
				l += 1
	return res