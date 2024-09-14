import re

def parse_line(line: str) -> (set[int], list[int]):
	header, game = line.split(':')
	identifier = int(re.findall(r'\d+', header)[0])
	l, r = game.split('|')
	wins = set(int(num) for num in re.findall(r'\d+', l))
	nums = set(int(num) for num in re.findall(r'\d+', r))
	return identifier, wins, nums

def part_one(filename: str) -> int:
	res: int = 0
	with open(filename) as f:
		for line in f:
			_, win, nums = parse_line(line)
			match = len(win.intersection(nums))
			if match > 0:
				res += 2**(match-1)
	return res

def part_two(filename: str) -> int:
	res: int = 0
	with open(filename) as f:
		instances = {i+1:1 for i in range(sum(1 for _ in f))}

	with open(filename) as f:
		for line in f:
			id, win, nums = parse_line(line)
			match = len(win.intersection(nums))
			for k in range(id+1,id+1+match):
				instances[k] += instances[id]
			
	return sum(instances.values())
	

def test(f, filename, expected):
	actual = f(filename)
	assert expected == actual, f"{f, filename}: expected {expected}, actual {actual}"

if __name__ == "__main__":
	test(part_one, 'input.txt', 23673)
	test(part_one, 'test1.txt', 13)

	test(part_two, 'input.txt', 12263631)
	test(part_two, 'test1.txt', 30)
