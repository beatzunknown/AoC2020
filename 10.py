with open('10.txt', 'r') as f:
    data = list(map(int, f.readlines()))
    jolts = sorted(data+[0, max(data)+3])

diff_1 = sum([jolts[i]-jolts[i-1]==1 for i in range(1, len(jolts))])
diff_3 = sum([jolts[i]-jolts[i-1]==3 for i in range(1, len(jolts))])
part_1 = diff_1 * diff_3
part_2 = 0

ways = [0 for i in range(jolts[-1]+1)]

# Edge cases for t_n where n < 3
ways[0] = 1
ways[jolts[1]] = 1
start = 2
if jolts[2] < 3:
    ways[jolts[2]] = 2
    start = 3

# DP: t_n = t_n-1 + t_n-2 + t_n-3
for i in jolts[start:]:
    ways[i] = sum(ways[i-3:i])
part_2 = ways[jolts[-1]]

print("Part 1:", part_1)
print("Part 2:", part_2)