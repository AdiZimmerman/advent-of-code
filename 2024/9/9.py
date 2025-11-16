def transform(lst):
	res = []
	num = 0
	for i in range(len(lst)):
		if i % 2 == 0:
			res += [str(num)]*int(lst[i])
			num += 1
		else:
			res += ['.']*int(lst[i])
	return res

def move(lst):
	l = 0
	r = len(lst) - 1
	while l < r:
		if lst[l] != '.':
			l += 1
			continue
		if lst[r] == '.':
			r -= 1
			continue
		lst[l], lst[r] = lst[r], lst[l]
		l += 1
		r -= 1
	return lst

def checksum(lst):
	s = 0
	for i in range(len(lst)):
		if lst[i] == '.':
			break
		s += int(lst[i])*i
	return s

def runs(lst):
	runs = []
	free_intervals = []
	idx = 0
	for i in range(len(lst)):
		if int(lst[i]) == 0:
			continue
		if i % 2 == 0:
			runs.append(int(lst[i]))
		else:
			free_intervals.append((idx, idx + int(lst[i])))
		idx += int(lst[i])
	return runs, free_intervals


with open('test.txt') as f:
	line = f.read()
runs, free_intervals = runs(line.strip())
print(runs, free_intervals)

for i in range(len(runs)):
	runs[len(runs)-1-i]
	for free_interval in free_intervals:
		if free_interval[1] - free_interval[0] < r:
#print(checksum(move(transform(list(line.strip())))))

