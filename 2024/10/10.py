grid = []
with open('input.txt') as f:
    for line in f:
        grid.append(list(line.strip()))
rows, cols = len(grid), len(grid[0])
R, C = rows, cols

directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
def path_sum(r, c, visited):
    if (r, c) in visited:
        return 0
    visited.add((r, c))

    if grid[r][c] == '9':
        return 1

    res = 0
    for d in directions:
        next_r, next_c = r + d[0], c + d[1]
        if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c].isnumeric() and int(grid[next_r][next_c]) == int(grid[r][c]) + 1:
            res += path_sum(next_r, next_c, visited)
    return res

def unique_paths(r, c):
    if grid[r][c] == '9':
        return 1
    
    res = 0
    for d in directions:
        next_r, next_c = r + d[0], c + d[1]
        if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c].isnumeric() and int(grid[next_r][next_c]) == int(grid[r][c]) + 1:
            res += unique_paths(next_r, next_c)
    return res

def unique_paths2(r, c, path, paths):
    if (r, c) in path:
        return
    
    path.append((r, c))
    
    if grid[r][c] == '9':
        paths.append(path.copy())
        path.pop()
        return
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc].isnumeric() and int(grid[nr][nc]) == int(grid[r][c]) + 1:
            unique_paths2(nr, nc, path, paths)
    
    path.pop()
    return

total_sum = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '0':
            score = path_sum(i, j, visited=set())
            total_sum += score

total_rating = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '0':
            rating = unique_paths(i, j)
            total_rating += rating

paths = []
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '0':
            unique_paths2(i, j, [], paths)

print(total_sum, total_rating, len(paths))
print(paths)