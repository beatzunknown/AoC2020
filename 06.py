groups = []
# add extra newline to input to work
with open('06.txt', 'r') as f:
    group = []
    for line in f.readlines():
        if (stripped := line.rstrip()):
            group.append(set(stripped))
        else:
            groups.append(group)
            group = []

part_1 = sum([len(set().union(*group)) for group in groups])
part_2 = sum([len(group[0].intersection(*group)) for group in groups])

print("Part 1:", part_1)
print("Part 2:", part_2)
