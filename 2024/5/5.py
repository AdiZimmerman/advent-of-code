from collections import defaultdict

def part_one():
	afters, updates = parse('input.txt')
	return calculate(afters, updates)

def part_two():
	afters, updates = parse('input.txt')
	return calculate2(afters, updates)

def parse(filename):
	afters = defaultdict(set)
	updates = []
	with open(filename) as f:
		for line in f:
			line = line[:-1]
			if len(line) == 0:
				continue
			elif len(line) == 5:
				afters[int(line[:2])].add(int(line[3:5]))
			else:
				updates.append([int(s) for s in line.split(',')])
	return afters, updates

def calculate(afters, updates):
	def helper(update):
		for i in range(len(update)):
			for j in range(i+1,len(update)):
				if update[i] in afters[update[j]]:
					return 0
		return update[len(update)//2]

	ans = 0
	for update in updates:
		ans += helper(update)
	return ans

def calculate2(afters, updates):
	def sort(update):
		total_swaps = 0
		n = len(update)
		while n > 0:
			for i in range(n-1):
				if update[i] in afters[update[i+1]]:
					update[i], update[i+1] = update[i+1], update[i]
					total_swaps += 1
			n -= 1
		return total_swaps

	ans = 0
	for update in updates:
		if sort(update) > 0:
			ans += update[len(update)//2]
	return ans
