def best_meeting_point_bf(grid):
	members = [[x,y] for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 1]
	min_distance = sys.maxsize
	for row in range(len(gird)):
		for col in range(len(grid[0])):
			distance = 0
			for member in members:
				distance += abs(row - member[0]) + abs(col - member[1])

			min_distance = min(min_distance, distance)


# min manhattan distance
def best_meeting_point(grid):
	members = [[x,y] for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 1]

	distance = 0
	members.sort(key=lambda member: member[0])
	x = members[len(members)/2][0]
	for member in members:
		distance += abs(member[0] - x)

	members.sort(key=lambda member: member[1])
	y = members[len(members)/2][1]
	for member in members:
		distance += abs(member[1] - y)

	return distance
