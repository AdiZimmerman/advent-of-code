filename = 'input.txt'
with open(filename) as f:
	line = f.readline()

def repeats_twice(idee: int) -> bool:
	idString = str(idee)
	if len(idString) % 2 != 0:
		return False
	if idString[:len(idString)//2] == idString[len(idString)//2:]:
		return True
	return False

def repeats_at_least_twice(idee: int) -> bool:
	idString = str(idee)
	chunk_sizes = []
	for i in range(1, len(idString)):
		if len(idString) % i == 0:
			chunk_sizes.append(i)

	for chunk_size in chunk_sizes:
		chunks = [idString[i:i + chunk_size] for i in range(0, len(idString), chunk_size)]
		if all(item == chunks[0] for item in chunks):
			return True

	return False


ranges = line.split(',')
part_one, part_two = 0, 0
for rang in ranges:
	startStr, endStr = rang.split('-')
	start, end = int(startStr), int(endStr)
	for idee in range(start, end + 1):
		if repeats_twice(idee):
			part_one += idee
		if repeats_at_least_twice(idee):
			part_two += idee

print(part_one, part_two)
