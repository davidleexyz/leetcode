# words中的word1和word2可能会重复
def shortest_word_distance(words, word1, word2):
	word1_index = -1
	word2_index = -1
	distance = float('inf')
	for idx, word in enumerate(words):
		if word == word1:
			word1_index.append(idx)

		if word == word2:
			word2_index.append(idx)

		if word1_index != -1 and word2_index != -1:
			distance = min(distance, abs(word1_index - word2_index))
	
	return distance

