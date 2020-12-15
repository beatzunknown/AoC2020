with open('15.txt', 'r') as f:
    memory = {int(e):i+1 for i, e in enumerate(n for n in f.readline().rstrip().split(','))}

for k in memory:
    if memory[k] == len(memory):
        prev = k
        break

for i in range(len(memory)+1, 30000001):
    if prev not in memory:
        diff = 0
    else:
        diff = i - 1 - memory[prev]
    memory[prev] = i-1
    prev = diff
    if i == 2020:
        part_1 = prev
part_2 = prev

print("Part 1:", part_1)
print("Part 2:", part_2)