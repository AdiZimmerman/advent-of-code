from collections import defaultdict

def part_one():
	left, right = [], []
	with open('input.txt') as f:
		for line in f:
			l, r = int(line[:5]), int(line[-6:])
			left.append(l)
			right.append(r)
	left.sort()
	right.sort()
	ans = 0
	for i in range(len(left)):
		ans += abs(left[i] - right[i])
	return ans	

def part_two():
	left = defaultdict(int)
	right = defaultdict(int)
	with open('input.txt') as f:
		for line in f:
			left[int(line[:5])] += 1
			right[int(line[-6:])] += 1
	ans = 0
	for num, count in left.items():
		ans += num * right[num] * count
	return ans
