with open('01.txt', 'r') as f:
    data = set([int(l.rstrip()) for l in f.readlines()])

target = 2020

def find_two(data, target):
    h_table = {}
    for x in data:
        diff = target-x
        if diff in h_table:
            return (diff, x)
        h_table[x] = diff
    return (-1, -1)

a, b = find_two(data, target)
part_1 = a * b

for x in data:
    y, z = find_two(data - set([x]), target-x)
    if y > 0 and x > 0:
        part_2 = x*y*z
        break

print("Part 1:", part_1)
print("Part 2:", part_2)
