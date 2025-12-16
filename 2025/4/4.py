filename = 'input.txt'
grid = [list(line.strip()) for line in open(filename)]

R, C = len(grid), len(grid[0])
directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

def remove():
	removed = []
	for r in range(R):
		for c in range(C):
			if grid[r][c] == '@':
				n = 0
				for d in directions:
					adjR, adjC = r + d[0], c + d[1]
					if 0 <= adjR < R and 0 <= adjC < C and grid[adjR][adjC] == '@':
						n += 1
				if n < 4:
					removed.append((r, c))

	for r, c in removed:
		grid[r][c] = '.'

	return len(removed)
				

def remove_until_end():
	part_one = remove()
	part_two = part_one

	while True:
		removed = remove()
		if removed == 0:
			return part_one, part_two
		part_two += removed

part_one, part_two = remove_until_end()
print(part_one, part_two)
