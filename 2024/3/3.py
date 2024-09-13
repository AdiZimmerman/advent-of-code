def part_one(filename: str) -> int:
	matrix = []
	with open(filename) as f:
		for line in f:
			matrix.append(list(line)[:-1]) # removes the next line character '\n'..

	rows, cols = len(matrix), len(matrix[0])

	def is_symbol(r, c) -> bool:
		return 0 <= r < rows and 0 <= c < cols and matrix[r][c] != "." and not matrix[r][c].isdigit()

	def adjacent_symbol(r, c) -> list[str]:
		for direction in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
			if is_symbol(r + direction[0], c + direction[1]):
				return True
		return False

	def find_num(r, c) -> int:
		found_adjacent_symbol = False
		n = 0
		while c < len(matrix[0]) and matrix[r][c].isdigit():
			n = n * 10 + int(matrix[r][c])
			if not found_adjacent_symbol:
				found_adjacent_symbol = adjacent_symbol(r, c)
			c += 1
		if not found_adjacent_symbol:
			return 0 # wipe the number if no symbol found..
		return n

	res: int = 0
	for r in range(rows):
		c = 0
		while c < cols:
			num = find_num(r, c)
			res += num
			c += len(str(num))
	return res

def part_two(filename: str) -> int:
	matrix = []
	with open(filename) as f:
		for line in f:
			matrix.append(list(line)[:-1]) # removes the next line character '\n'..

	def expand_num(r, c, seen) -> int:
		while c > 0 and matrix[r][c-1].isdigit():
			c -= 1
		n = 0
		while c < len(matrix[0]) and matrix[r][c].isdigit():
			seen.add((r, c))
			n = n * 10 + int(matrix[r][c])
			c += 1
		return n

	rows, cols = len(matrix), len(matrix[0])
	def gear_ratio(r, c) -> int:
		seen = set()
		nums = []
		for direction in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
			adj_r = r + direction[0]
			adj_c = c + direction[1]
			if 0 <= adj_r < rows and 0 <= adj_c < cols and matrix[adj_r][adj_c].isdigit() and (adj_r, adj_c) not in seen:
				nums.append(expand_num(adj_r, adj_c, seen))
		if len(nums) != 2:
			return 0
		return nums[0] * nums[1]

	res: int = 0
	for r in range(rows):
		for c in range(cols):
			if matrix[r][c] == '*':
				res += gear_ratio(r, c)
	return res


def test(f, filename, expected):
	actual = f(filename)
	assert expected == actual, f"{f, filename}: expected {expected}, actual {actual}"

if __name__ == "__main__":
	test(part_one, 'input.txt', 527369)
	test(part_one, 'test1.txt', 4361)
	test(part_one, 'test2.txt', 413)
	test(part_one, 'test3.txt', 925)
	test(part_one, 'test4.txt', 4)
	test(part_one, 'test5.txt', 0)
	test(part_one, 'test6.txt', 156)
	test(part_one, 'test7.txt', 40)
	test(part_one, 'test8.txt', 62)

	test(part_two, 'input.txt', 73074886)
	test(part_two, 'test1.txt', 467835)
	test(part_two, 'test2.txt', 6756)
	test(part_two, 'test3.txt', 6756)
	test(part_two, 'test4.txt', 0)
	test(part_two, 'test5.txt', 0)
	test(part_two, 'test6.txt', 0)
	test(part_two, 'test7.txt', 442)
	test(part_two, 'test8.txt', 478)

