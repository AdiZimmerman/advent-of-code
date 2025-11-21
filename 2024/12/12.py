"""
- - - -
A|A|A|A|
- - - -
B|B|C|D|
- - - -
B|B|C|C|
- - - -
E|E|E|C|
- - - -


(0,0),(0,1)
"""

from collections import defaultdict

def parse_grid_from_file(filename: str) -> list[list[str]]:
    return [list(line.strip()) for line in open(filename)]

grid = parse_grid_from_file('test.txt')
R, C = len(grid), len(grid[0])
visited = set()

dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))

def dfs(i, j):
    if (i, j) in visited:
        return 0, 0
    visited.add((i, j))
    area = 1
    perim = 0

    # up
    if i == 0 or grid[i][j] != grid[i-1][j]:
        perim += 1
    else:
        a, p = dfs(i - 1, j)
        area += a
        perim += p
    # left
    if j == 0 or grid[i][j] != grid[i][j-1]:
        perim += 1
    else:
        a, p = dfs(i, j - 1)
        area += a
        perim += p
    # down
    if i == R - 1 or grid[i][j] != grid[i+1][j]:
        perim += 1
    else:
        a, p = dfs(i + 1, j)
        area += a
        perim += p
    # right
    if j == C - 1 or grid[i][j] != grid[i][j+1]:
        perim += 1
    else:
        a, p = dfs(i, j + 1)
        area += a
        perim += p

    return area, perim

def dfs2(cur, prev):
    if cur in visited:
        return 0, 0
    visited.add(cur)

    i, j = cur
    pi, pj = prev

    area = 1
    perim = 0

    # up
    if i == 0 or grid[i][j] != grid[i-1][j]:
        if abs(i - pi) > 0:
            print(cur, prev)
            perim += 1
    else:
        a, p = dfs2((i-1, j), (i, j))
        area += a
        perim += p
    # left
    if j == 0 or grid[i][j] != grid[i][j-1]:
        if abs(j - pj) > 0:
            print(cur, prev)
            perim += 1
    else:
        a, p = dfs2((i, j - 1), (i, j))
        area += a
        perim += p
    # down
    if i == R - 1 or grid[i][j] != grid[i+1][j]:
        if abs(i - pi) > 0:
            print(cur, prev)
            perim += 1
    else:
        a, p = dfs2((i + 1, j), (i, j))
        area += a
        perim += p
    # right
    if j == C - 1 or grid[i][j] != grid[i][j+1]:
        if abs(j - pj) > 0:
            print(cur, prev)
            perim += 1
    else:
        a, p = dfs2((i, j + 1), (i, j))
        area += a
        perim += p

    return area, perim

res = 0
for i in range(R):
    for j in range(C):
        if (i, j) not in visited:
            area, perim = dfs2((i, j), (-1, -1))
            print(f"{grid[i][j]}, area {area}, perim {perim}")
            res += area * perim
print(res)



