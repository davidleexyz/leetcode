# find integers a, b, c in nums, that a + b + c is closet to target t
import math

def three_sum_cloest(nums, target):
	nums.sort()
	result = float("inf")
	diff = float("inf")
	for i in range(len(nums)):
		if i > 0 and nums[i] == nums[i-1]:
			continue

		l,r = i+1, len(nums)-1
		while l < r:
			res = nums[i] + nums[l] + nums[r]
			tmp = res - target
			if tmp == 0:
				return res
			elif tmp > 0:
				if diff > math.fabs(tmp):
					diff = math.fabs(tmp)
					result = res
				r -= 1
			else:
				if diff > math.fabs(tmp):
					diff = math.fabs(tmp)
					result = res
				l += 1
	return result