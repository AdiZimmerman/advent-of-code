filename = 'input.txt'
lines = [line.strip() for line in open(filename)]

def part_one() -> int:
	position = 50
	ans = 0
	for line in lines:
		direction = line[0]
		rotation = int(line[1:])
		mul = 1 if direction == 'R' else -1
		tmp = position + (mul * rotation)

		# calculate
		if tmp % 100 == 0:
			ans += 1

		tmp = tmp % 100
		position = tmp
	return ans

def part_two() -> int:
	position = 50
	ans = 0
	for line in lines:
		direction = line[0]
		rotation = int(line[1:])
		mul = 1 if direction == 'R' else -1
		tmp = position + (mul * rotation)

		# calculate
		passed = 0
		if tmp == 0:
			ans += 1
		elif tmp > 0:
			passed = tmp // 100
		else: # tmp < 0
			passed = abs(tmp // 100) - (position == 0) + (tmp % 100 == 0)
		ans += passed

		tmp = tmp % 100
		position = tmp
	return ans

print(part_one())
print(part_two())