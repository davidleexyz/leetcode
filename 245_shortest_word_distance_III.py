def shortest_word_distance_III(words, word1, word2):
	word1_idx = -1
	word2_idx = -1
	distance = float('inf')

	for idx, word in enumerate(words):
		if word1 == word2:
			if word == word1:
				word2_idx = word1_idx
				word1_idx = idx
		else:
			if word == word1:
				word1_idx = idx

			if word == word2:
				word2_idx = idx

		if word1_idx != -1 and word2_idx != -1:
			distance = min(distance, abs(word1_idx - word2_idx))

	return distance