
from collections import defaultdict

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def part_one():
	grid, pos = parse('input.txt')
	i = 0
	path = []
	while True:
		path.append(pos)
		nxt = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
		if 0 <= nxt[0] < len(grid) and 0 <= nxt[1] < len(grid[0]):
			if grid[nxt[0]][nxt[1]] == '#':
				i = (i + 1) % 4
			else:
				pos = nxt
		else:
			break
	return len(set(path))

def part_two():
	grid, start = parse('input.txt')
	i = 0
	pos = start
	path = []
	while True:
		nxt = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
		if 0 <= nxt[0] < len(grid) and 0 <= nxt[1] < len(grid[0]):
			if grid[nxt[0]][nxt[1]] == '#':
				i = (i + 1) % 4
			else:
				path.append(nxt)
				pos = nxt
		else:
			break
	
	ans = set()
	for p in path:
		if p in ans:
			continue
		grid[p[0]][p[1]] = '#'
		if search(grid,start,0):
			ans.add(p)
		grid[p[0]][p[1]] = '.'
	return len(ans)

def search(grid, pos, i):
	prev = defaultdict(set)
	while True:
		prev[i].add(pos)
		nxt = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
		if 0 <= nxt[0] < len(grid) and 0 <= nxt[1] < len(grid[0]):
			if grid[nxt[0]][nxt[1]] == '#':
				i = (i + 1) % 4
			else:
				if nxt in prev[i]:
					return 1
				pos = nxt
		else:
			break
	return 0

def parse(filename):
	lines = []
	with open(filename) as f:
		lines = f.readlines()
	grid = []
	pos = None
	for r in range(len(lines)):
		row = []
		for c in range(len(lines[r][:-1])):
			if lines[r][c] == '^':
				row.append('.')
				pos = (r, c)
			else:
				row.append(lines[r][c])
		grid.append(row)
	return grid, pos
