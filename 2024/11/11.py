from collections import defaultdict

count = {}
with open('input.txt') as f:
    stones = f.read().split()
    count = {stone:stones.count(stone) for stone in set(stones)}

N = 75
for _ in range(N):
    new_count = defaultdict(int)
    for stone, num in count.items():
        if stone == '0':
            new_count['1'] += num
        elif len(stone) % 2 == 0:
            new_count[str(int(stone[:len(stone)//2]))] += num
            new_count[str(int(stone[len(stone)//2:]))] += num
        else:
            new_count[str(int(stone)*2024)] += num
    count = new_count

print(f"Unique stones: {len(count)}\nTotal stones: {sum(count.values())}") 