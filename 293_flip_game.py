def flip_game(s):
	if not s:
		return []

	res = []
	for i in range(len(s)):
		if s[i] == '+' and s[i+1] == '+':
			res.append(s[:i] + '--' + s[i+2:])

	return res
