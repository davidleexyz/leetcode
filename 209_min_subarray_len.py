# 理解题意  consecutive subarray 不是指数组的内容连续
# 先找到和满足条件的子数组 然后再找最小长度
def min_subarray_len(s, nums):
	import sys

	start, end, sums, length = 0, 0, 0, sys.maxsize
	while end < len(nums):
		sums += nums[end]
		end += 1
		while sums >= s:
			sums -= nums[start]
			start += 1
			length = min(length, end-start+1)
	return length if length != sys.maxsize else 0