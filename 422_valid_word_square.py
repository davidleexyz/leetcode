def valid_word_square(words):

	for i in range(len(words)):
		horizontal = words[i]
		vertial = ''
		for j in range(len(words)):
			vertical += words[j][i]

		if horizontal != vertical:
			return False

	return True