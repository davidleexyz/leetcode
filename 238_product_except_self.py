def product_except_self(nums):
	prefix_product = [1] * len(nums)
	suffix_product = [1] * len(nums)

	for i in range(1, len(nums)):
		prefix_product[i] = prefix_product[i-1] * nums[i-1]

	for i in reversed(range(0, len(nums)-1)):
		suffix_product[i] = suffix_product[i+1] * nums[i+1]

	res = []

	for i in range(len(nums)):
		product = prefix_product[i] * suffix_product[i]

		res.append(product)

	return res