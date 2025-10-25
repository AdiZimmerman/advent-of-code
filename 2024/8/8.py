from collections import defaultdict

grid = []
with open('input.txt') as f:
    for line in f:
        grid.append(list(line.strip()))
rows, cols = len(grid), len(grid[0])

antennas = defaultdict(list)
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '.':
            continue
        antennas[grid[r][c]].append((r, c))

def antinodes(pair, rows, cols):
    one, two = pair[0], pair[1]
    dx, dy = two[0] - one[0], two[1] - one[1]
    three = (one[0] - dx, one[1] - dy)
    four = (two[0] + dx, two[1] + dy)
    return [p for p in (three, four) if 0 <= p[0] < rows and 0 <= p[1] < cols]

def antinodes_unlimited(pair, rows, cols):
    one, two = pair[0], pair[1]
    dx, dy = two[0] - one[0], two[1] - one[1]

    locations = []
    while 0 <= one[0] < rows and 0 <= one[1] < cols:
        locations.append(one)
        one = (one[0] - dx, one[1] - dy)

    while 0 <= two[0] < rows and 0 <= two[1] < cols:
        locations.append(two)
        two = (two[0] + dx, two[1] + dy)

    return locations

def pairs():
    pairs = []
    for group in antennas.values():
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                pairs.append((group[i], group[j]))
    return pairs

def part_one():
    ans = set()
    for pair in pairs():
        for location in antinodes(pair, rows, cols):
            ans.add(location)
    return len(ans)

def part_two():
    ans = set()
    for pair in pairs():
        for location in antinodes_unlimited(pair, rows, cols):
            ans.add(location)
    return len(ans)
