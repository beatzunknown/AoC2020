import math

rules = {}
my_ticket = []
other_tickets = []

with open('16.txt', 'r') as f:
    while l:=f.readline().rstrip():
        k, v = l.split(': ')
        rules[k] = [list(map(int, r.split('-'))) for r in v.split(' or ')]
    f.readline()
    my_ticket = list(map(int, f.readline().rstrip().split(',')))
    f.readline()
    f.readline()
    other_tickets = [list(map(int, l.rstrip().split(','))) for l in f.readlines()]

in_range = lambda v, r: (r[0][0] <= v <= r[0][1]) or (r[1][0] <= v <= r[1][1])
passes_rules = lambda rules, v: any(in_range(v, r) for r in rules.values())
get_invalids = lambda r, t: [n for n in t if not passes_rules(r, n)]

invalid_sum = 0
invalid_tickets = []
for ticket in other_tickets:
    invalids = get_invalids(rules, ticket)
    if invalids:
        invalid_sum += sum(invalids)
        invalid_tickets.append(ticket)

for ticket in invalid_tickets:
    other_tickets.remove(ticket)

possibilities = {}
for field in rules:
    for i in range(len(my_ticket)):
        if all(in_range(ticket[i], rules[field]) for ticket in other_tickets):
            possibilities[field] = possibilities.get(field, []) + [i]

possibilities = sorted([(k, v) for k, v in possibilities.items()], key=lambda x: len(x[1]))

fields = {}
for i in range(len(possibilities)):
    field, pos = possibilities[i]
    pos = pos[0]
    fields[field] = pos
    for i in range(i, len(possibilities)):
        possibilities[i][1].remove(pos)

my_ticket = {field:my_ticket[fields[field]] for field in fields}
prod = math.prod([v for k,v in my_ticket.items() if k.startswith('departure')])

print("Part 1:", invalid_sum)
print("Part 2:", prod)