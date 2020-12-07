import re

data = []
with open('04.txt', 'r') as f:
    entry = {}
    # only add entries which are valid
    for line in f.readlines():
        if not line.rstrip():
            entry.pop('cid', None)
            if len(entry.keys()) == 7:
                data.append(entry)
            entry = {}
            continue

        for kv_pair in line.rstrip().split():
            k,v = kv_pair.split(':')
            entry[k] = v
    # technically I should add the last entry here
    # but adding an extra newline to input lets me
    # avoid that by forcing the loop to run another time

part_1 = len(data)
part_2 = 0

for e in data:
    byr = int(e['byr'])
    iyr = int(e['iyr'])
    eyr = int(e['eyr'])
    hgt = e['hgt']
    hcl = e['hcl']
    ecl = e['ecl']
    pid = e['pid']

    if not (1920<=byr<=2002):
        continue
    if not (2010<=iyr<=2020):
        continue
    if not (2020<=eyr<=2030):
        continue
    if hgt[-2:] == 'cm':
        if not (150<=int(hgt[:-2])<=193):
            continue
    elif hgt[-2:] == 'in':
        if not (59<=int(hgt[:-2])<=76):
            continue
    else: 
        continue
    if not re.match(r'^#([\da-f]){6}$', hcl):
        continue
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        continue
    if not re.match(r'^\d{9}$', pid):
        continue
    part_2 += 1

print("Part 1:", part_1)
print("Part 2:", part_2)