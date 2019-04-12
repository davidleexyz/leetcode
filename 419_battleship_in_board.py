def count_battleships(board):
	if not board or not board[0]:
		return 0

	count = 0
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 'X':
				if (not i or board[i-1][j] == '.') and (not j or board[i][j-1] == '.'):
					count += 1

	return count

