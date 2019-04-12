def find_lonely_pixel(picture):
	cord_x = []
	cord_y = []
	for i in range(len(picture)):
		for j in range(len(picture[0])):
			if picture[i][j] == 'B':
				cord_x.append(i)
				cord_y.append(j)

	cord_xx = []
	cord_yy = []
	for i, x in enumerate(cord_x):
		if cord_x.count(x) == 1:
			cord_xx.append(x)
			cord_yy.append(cord_y[i])

	res = 0
	for i, y in enumerate(cord_yy):
		if cord_yy.count(y) == 1:
			res += 1

	return res







