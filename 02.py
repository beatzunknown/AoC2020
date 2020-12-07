import re

pattern = re.compile(r'(\d+)-(\d+) ([a-z]): (\w+)')
data = []

with open('02.txt', 'r') as f:
    data = [pattern.search(line.rstrip()).groups() for line in f.readlines()]

# a is lowerbound, b is upperbound, c is character, d is password string
data = [(int(a),int(b),c,d) for a,b,c,d in data]

part_1 = sum([a<=d.count(c)<=b for a,b,c,d in data])

# -1 to account for 1-indexed password
# XOR logic as character can only be in password at 1 of the 2 positions a,b
part_2 = sum([bool(d[a-1]==c)^bool(d[b-1]==c) for a,b,c,d in data])

print("Part 1:", part_1)
print("Part 2:", part_2)