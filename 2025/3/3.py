filename = 'input.txt'
lines = [line.strip() for line in open(filename)]

# how many digits per line
# part one -> set K to 2
# part two -> set K to 12
K = 12

ans = 0
for line in lines:
	chars = list(line)
	maximums = []

	# K scans for maximum, starting from previous max and ending with enough space to fit remaining digits in
	m, idx = -1, -1
	for k in range(K-1,-1,-1):
		for i in range(idx + 1, len(chars) - k):
			n = int(chars[i])
			if n > m:
				m, idx = n, i
		maximums.append(m)
		m = -1
	ans += int(''.join([str(m) for m in maximums]))

print(ans)
