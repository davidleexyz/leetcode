# dp[i] = max(dp[k] + 1, if a[i] > a[k])
def increasing_triplet_subsequence_dp(nums):
	dp = [1] * len(nums)

	for i in range(1, len(nums)):
		j = 0 
		while j < i:
			if nums[i] > nums[j]:
				dp[i] = max(dp[j] + 1, dp[i])
			j += 1

	if max(dp) >= 3:
		return True
	else:
		return False

def increasing_triplet_subsequence(nums):
	if len(nums) < 3:
		return False

	first, second = float('inf'), float('inf')
	for num in nums:
		if num <= first:
			first = num
		elif num <= second:
			second = num
		else:
			return True
	return False