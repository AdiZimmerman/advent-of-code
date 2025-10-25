import re
from collections import namedtuple
import bisect


def part_one(filename: str) -> int:
	res: int = 0
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(line[:-1]) # removes the next line character '\n'..

	indeces = [-1, -1, -1, -1, -1, -1, -1]
	for i, line in enumerate(lines):
		if line.startswith('seeds:'):
			seeds = [int(num) for num in re.findall(r'\d+', line.split(':')[1])]
		elif line.startswith('seed-to-soil map:'):
			indeces[0] = i+1
		elif line.startswith('soil-to-fertilizer map:'):
			indeces[1] = i+1
		elif line.startswith('fertilizer-to-water map:'):
			indeces[2] = i+1
		elif line.startswith('water-to-light map:'):
			indeces[3] = i+1
		elif line.startswith('light-to-temperature map:'):
			indeces[4] = i+1
		elif line.startswith('temperature-to-humidity map:'):
			indeces[5] = i+1
		elif line.startswith('humidity-to-location map:'):
			indeces[6] = i+1

	def create(lines: list[str], start: int) -> dict:
		m = []
		while start < len(lines) and lines[start] != '':
			nums = [int(num) for num in re.findall(r'\d+', lines[start])]
			to, frm, k = int(nums[0]), int(nums[1]), int(nums[2])
			bisect.insort_left(m, (frm, to, k))
			start += 1
		return m

	sorted_maps = []
	for i in indeces:
		sorted_maps.append(create(lines, i))

	res: int = float('inf')
	for seed in seeds:
		cur = seed
		for m in sorted_maps:
			idx = bisect.bisect(m, cur, key=lambda tup: tup[0]) - 1
			frm, to, k = m[idx]
			if frm <= cur < frm + k:
				cur += to - frm		
		res = min(res, cur)

	return res
	

def part_two(filename: str) -> int:
	res: int = 0
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(line[:-1]) # removes the next line character '\n'..

	indeces = [-1, -1, -1, -1, -1, -1, -1]
	seeds = []
	for i, line in enumerate(lines):
		if line.startswith('seeds:'):
			nums = [int(num) for num in re.findall(r'\d+', line.split(':')[1])]
			seeds = [(nums[i], nums[i] + nums[i+1]) for i in range(0, len(nums), 2)]
		elif line.startswith('seed-to-soil map:'):
			indeces[0] = i+1
		elif line.startswith('soil-to-fertilizer map:'):
			indeces[1] = i+1
		elif line.startswith('fertilizer-to-water map:'):
			indeces[2] = i+1
		elif line.startswith('water-to-light map:'):
			indeces[3] = i+1
		elif line.startswith('light-to-temperature map:'):
			indeces[4] = i+1
		elif line.startswith('temperature-to-humidity map:'):
			indeces[5] = i+1
		elif line.startswith('humidity-to-location map:'):
			indeces[6] = i+1

	def create(lines: list[str], start: int) -> dict:
		m = []
		while start < len(lines) and lines[start] != '':
			nums = [int(num) for num in re.findall(r'\d+', lines[start])]
			to, frm, k = int(nums[0]), int(nums[1]), int(nums[2])
			bisect.insort_left(m, (frm, to, k))
			start += 1
		return m

	sorted_maps = []
	for i in indeces:
		sorted_maps.append(create(lines, i))

	res: int = float('inf')
	for start, end in seeds:
		for seed in range(start, end):
			cur = seed
			for m in sorted_maps:
				idx = bisect.bisect(m, cur, key=lambda tup: tup[0]) - 1
				frm, to, k = m[idx]
				if frm <= cur < frm + k:
					cur += to - frm

			res = min(res, cur)

	return res

def test(f, filename, expected):
	actual = f(filename)
	assert expected == actual, f"{f, filename}: expected {expected}, actual {actual}"

if __name__ == "__main__":
	print(part_two('test1.txt'))
