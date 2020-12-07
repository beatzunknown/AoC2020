import re

# key contains values
contains = {}
# key is_in values
is_in = {}

with open('07.txt', 'r') as f:
    for line in f.readlines():
        line = line.rstrip()
        container = ' '.join(line.split()[:2])
        contains[container] = re.findall(r'(\d) (\w+ \w+)', line)
        for num, item in contains[container]:
            is_in[item] = is_in.get(item, list()) + [(num, container)]

contains_gold = set()
queue = [('shiny gold')]
while queue:
    entry = queue.pop()
    if entry in is_in:
        for num, container in is_in[entry]:
            contains_gold |= {container}
            queue.append(container)
part_1 = len(contains_gold)

part_2 = 0
queue = [(int(a), b) for a,b in contains['shiny gold']]
while queue:
    num, bag = queue.pop()
    part_2 += num
    if contains[bag]:
        for num2, bag2 in contains[bag]:
            queue.append((num*int(num2), bag2))

print("Part 1:", part_1)
print("Part 2:", part_2)
