filename = 'input.txt'
lines = [line.strip() for line in open(filename)]

position = 50
part_one, part_two = 0, 0
for line in lines:
	rotation = int(line[1:]) * (1 if line[0] == 'R' else -1)
	tmp = position + rotation

	part_one += tmp % 100 == 0

	if tmp == 0:
		part_two += 1
	elif tmp > 0:
		part_two += tmp // 100
	else: # tmp < 0
		part_two += abs(tmp // 100) - (position == 0) + (tmp % 100 == 0)

	position = tmp % 100

print(part_one, part_two)
