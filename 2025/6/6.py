filename = 'input.txt'
grid = [list(line.split()) for line in open(filename)]
R, C = len(grid), len(grid[0])
part_one = 0
for c in range(C):
	if grid[R-1][c] == '+':
		tmp = sum(int(grid[r][c]) for r in range(R-1))
		part_one += tmp
	else:
		tmp = 1
		for r in range(R-1):
			tmp *= int(grid[r][c])
		part_one += tmp

lines = [line[:len(line)-1] for line in open(filename)]
operators = []
for i in range(len(lines[-1])):
	if lines[-1][i] != ' ':
		operators.append(i)
part_two = 0
for o in range(len(operators)):
	start_column = operators[o+1]-2 if o+1 < len(operators) else len(lines[-1])-1
	end_column = operators[o]
	nums = []
	for c in range(start_column, end_column-1, -1):
		nums.append(int(''.join(line[c] for line in lines[:len(lines)-1])))
	if lines[-1][end_column] == '+':
		part_two += sum([int(n) for n in nums])
	else:
		tmp = 1
		for n in nums:
			tmp *= int(n)
		part_two += tmp

print(part_one, part_two)

