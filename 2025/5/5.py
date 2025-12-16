filename = 'input.txt'
lines = [line.strip() for line in open(filename)]

intervals = []
ids = []
for line in lines:
	parts = line.split('-')
	if len(parts) == 2:
		intervals.append((int(parts[0]), int(parts[1])))
	if len(parts) == 1 and parts[0]:
		ids.append(int(parts[0]))

def inside(i):
	for start, end in intervals:
		if start <= i <= end:
			return True
	return False

part_one = 0
for i in ids:
	part_one += int(inside(i))

def merge_intervals(intervals):
	intervals.sort(key=lambda interval: interval[0])
	merged = [intervals[0]]
	for i in range(1, len(intervals)):
		if merged[-1][1] >= intervals[i][0]:
			merged[-1] = (merged[-1][0], max(merged[-1][1], intervals[i][1]))
		else:
			merged.append(intervals[i])
	return merged

merged_intervals = merge_intervals(intervals)
part_two = sum(end - start + 1 for start, end in merged_intervals)

print(part_one, part_two)
