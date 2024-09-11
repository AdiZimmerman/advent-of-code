def part_one(filename: str) -> int:
	matrix = []
	with open(filename) as f:
		for line in f:
			matrix.append(list(line))

	rows, cols = len(matrix), len(matrix[0])

	def is_symbol(r, c) -> bool:
		return 0 <= r < rows and 0 <= c < cols and matrix[r][c] != "." and not matrix[r][c].isdigit()

	def adjacent_symbol(r, c) -> list[str]:
		for direction in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
			if is_symbol(r + direction[0], c + direction[1]):
				return True
		return False

	def find_num(r, c) -> int:
		valid = False
		n = 0
		while c < len(matrix[0]) and matrix[r][c].isdigit():
			n = n * 10 + int(matrix[r][c])
			if not valid:
				valid = adjacent_symbol(r, c)
			c += 1
		if valid:
			return n
		return 0

	res: int = 0
	for r in range(rows):
		c = 0
		while c < cols:
			num = find_num(r, c)
			res += num
			c += len(str(num))
	return res


def test(f, filename, expected):
	actual = f(filename)
	assert expected == actual, f"{f, filename}: expected {expected}, actual {actual}"

if __name__ == "__main__":
	print(part_one('input.txt'))