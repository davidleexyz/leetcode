def game_of_life(board):
	res = []
	directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
	for row in range(len(board)):
		for col in range(len(board[0])):
			positions = [[row + x, col + y] for x, y in directions]
			live_neighbors = 0
			for pos in positions:
				neighbor_row, neighbor_col = pos
				if neighbor_row >= 0 and neighbor_row < len(board) and neighbor_col >= 0 and neighbor_col < len(board[0]):
					if board[neighbor_row][neighbor_col] == 1:
						live_neighbors += 1
					
			if board[row][col] == 1:
				if live_neighbors == 2 or live_neighbors == 3:
					res.append(1)
				else:
					res.append(0)
			else:
				if live_neighbors == 3:
					res.append(1)
				else:
					res.append(0)

	print(len(res))
	index = 0
	for row in range(len(board)):
		for col in range(len(board[0])):
			board[row][col] = res[index]
			index += 1