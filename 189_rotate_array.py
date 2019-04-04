def rotate_array_tle(nums, k):
	while k > 0:
		tmp = nums[-1]
		for i in reversed(range(1, len(nums))):
			nums[i] = nums[i-1]
		nums[0] = tmp
		k -= 1

def rotate_array_math(nums, k):
	if k != 0:
		k = k % len(nums)
		nums[:-k] = reversed(nums[:-k])
		nums[-k:] = reversed(nums[-k:])
		nums[:] = reversed(nums)


def rotate_array(nums, k):
	k = k % len(nums)
	nums[:] = nums[-k:] + nums[:-k]

