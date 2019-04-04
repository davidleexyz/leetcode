def plus_one(digits):
	integer = 0
	for digit in digits:
		integer *= 10
		integer += digit

	integer += 1
	res = []
	while integer > 0:
		digit = integer % 10
		integer //= 10
		res.insert(0, digit)
	return res