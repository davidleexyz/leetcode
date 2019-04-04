# time limit exceeded
def next_permutation_tle(nums):	
	def calculate(l):
		base = 0
		for num in l:
			base += num * 10
		return base

	base = calculate(nums)
	n = len(nums)
	index = n - 1
	while index >= 0:
		nums[index-1], nums[index] = nums[index], nums[index-1]
		res = calculate(nums)
		if res > base:
			return

	nums.sort()


def next_permutation(nums):

	index = -1
	for i in range(len(nums)-1, 0, -1):
		if nums[i] > nums[i-1]:
			index = i - 1
			break

	if index >= 0:
		for i in range(len(nums)-1, index, -1):
			if nums[i] > nums[index]:
				nums[index], nums[i] = nums[i], nums[index]
				break;

	nums[index+1:] = nums[index+1:][::-1]
