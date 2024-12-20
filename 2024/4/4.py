from collections import defaultdict

def part_one():
	with open('input.txt') as f:
		grid = []
		for line in f:
			grid.append(list(line)[:-1])
		return count(grid)

def part_two():
	with open('input.txt') as f:
		grid = []
		for line in f:
			grid.append(list(line)[:-1])
		return count2(grid)

def count(grid):
	ans = 0
	letters = ['X','M','A','S']
	directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
	
	def found(r, c, d):
		for k in range(4):
			next_r = r + d[0]*k
			next_c = c + d[1]*k
			if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]) and grid[next_r][next_c] == letters[k]:
				continue
			return 0
		return 1

	for r in range(len(grid)):
		for c in range(len(grid[0])):
				ans += sum(found(r, c, d) for d in directions)
	return ans


def count2(grid):
	ans = 0
	def found(r, c):
		if grid[r][c] != 'A':
			return 0
		letters = defaultdict(list)
		for d in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
			next_r = r + d[0]
			next_c = c + d[1]
			if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]):
				letters[grid[next_r][next_c]].append(d)
		if len(letters['M']) != 2 or len(letters['S']) != 2:
			return 0
		# you can consider 'M' or 'S' b/c if one of them is not next to each other the other is too
		m1 = letters['M'][0]
		m2 = letters['M'][1]
		if m1[0] + m2[0] == 0 and m1[1] + m2[1] == 0:
			return 0
		return 1

	for r in range(len(grid)):
		for c in range(len(grid[0])):
				ans += found(r, c)
	return ans
