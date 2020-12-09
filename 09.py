with open('09.txt', 'r') as f:
    data = list(map(int, f.readlines()))

sums = set()
sums = [x+y for x in data[:25] for y in data[:25] if x != y]

part_1 = 0
for i in range(len(data)-25):
    j = i+25
    if data[j] not in sums:
        part_1 = data[j]
        break
    for num in data[i+1:j]:
        sums.remove(num+data[i])
    sums += [data[j]+num for num in data[i+1:j]]

part_2 = 0
for i in range(len(data)-1):
    for j in range(i, len(data)):
        if (j-i) > 1:
            contiguous = data[i:j+1]
            if sum(contiguous) == part_1:
                part_2 = min(contiguous) + max(contiguous)

print("Part 1:", part_1)
print("Part 2:", part_2)
