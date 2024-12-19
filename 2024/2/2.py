def part_one():
	ans = 0
	with open('input.txt') as f:
		for line in f:
			ans += safe(line.split(' '))
	return ans

def part_two():
	ans = 0
	with open('input.txt') as f:
		for line in f:
			ans += safe(line.split(' '),True)
	return ans

def safe(reports, remove=False):
	inc = 0
	i = 0
	errors = 0
	while i < len(reports)-1:
		cur, nxt = int(reports[i]), int(reports[i+1])
		diff = cur - nxt
		wrong_way = inc != 0 and (diff > 0 and inc == 1) or (diff < 0 and inc == -1)
		differ = abs(diff) < 1 or abs(diff) > 3
		if wrong_way or differ:
			if remove:
				return safe(reports[1:],False) or safe(reports[:i]+reports[i+1:],False) or safe(reports[:i+1]+reports[i+2:],False)
			return 0
		inc = -1 if diff > 0 else 1
		i += 1
	return 1
