def place_flowers(flowerbed, n):
	if not flowerbed:
		return False

	if n == 0:
		return True

	if len(flowerbed) == 1:
		if flowerbed[0] == 1:
			return False
		else:
			return True

	for i in range(len(flowerbed)):
		if flowerbed[i] == 0 and i == 0 and flowerbed[i+1] == 0:
			flowerbed[i] = 1
			n -= 1
			continue

		if flowerbed[i] == 0 and i == len(flowerbed) -1 and flowerbed[i-1] == 0:
			flowerbed[i] = 1
			n -= 1
			continue

		if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
			flowerbed[i] = 1
			n -= 1

	if n <= 0:
		return True
	else:
		return False

