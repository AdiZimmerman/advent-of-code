import math
from collections import defaultdict

def part_one(filename: str) -> int:
	TOTAL = {"red": 12, "green": 13, "blue": 14}

	def parse_line(line: str) -> (int, dict):
		header, body = line.split(':')
		identifier = int(header.split(' ')[1])
		subsets = []
		for subset in body.split(';'):
			d = dict()
			for item in subset.split(','):
				num, color = item.strip().split(' ')
				d[color] = int(num)
			subsets.append(d)
		return identifier, subsets

	def valid(subsets: list[dict]) -> bool:
		for subset in subsets:
			remaining = TOTAL.copy()
			for color, num in subset.items():
				remaining[color] -= num
				if remaining[color] < 0:
					return False
		return True

	with open(filename) as f:
		res: int = 0
		for line in f:
			identifier, subsets = parse_line(line)
			if valid(subsets):
				res += identifier
	return res

def part_two(filename: str) -> int:
	with open(filename) as f:
		res: int = 0
		for line in f:
			header, body = line.split(':')
			identifier = int(header.split(' ')[1])
			maxes = defaultdict(int)
			for subset in body.split(';'):
				d = dict()
				for item in subset.split(','):
					num, color = item.strip().split(' ')
					d[color] = int(num)
				for color in d:
					maxes[color] = max(maxes[color], d[color])
			res += math.prod([v for v in maxes.values()])
	return res

def test(f, filename, expected):
	actual = f(filename)
	assert expected == actual, f"{f, filename}: expected {expected}, actual {actual}"

if __name__ == "__main__":
	test(part_one, 'test1.txt', 8)
	test(part_one, 'input.txt', 2563)
	test(part_two, 'test1.txt', 2286)
	test(part_two, 'input.txt', 70768)
