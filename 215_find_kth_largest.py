def find_kth_largest(nums, k):
	import heapq

	res = heapq.nlargest(k, nums)

	return res[-1]