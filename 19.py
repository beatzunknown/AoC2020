texts = []
rules = []
with open('19.txt', 'r') as f:
    while l:= f.readline().rstrip():
        rules.append(l)
    texts = [l.rstrip() for l in f.readlines()]

def build_rules(rules):
    parsed_rules = []
    for rule in rules:
        k, v = rule.split(': ')
        if v[1].isalpha():
            parsed_rules.append((k, v[1]))
        else:
            v = [x.split() for x in v.split(' | ')]
            parsed_rules.append((k, v))
    return parsed_rules

def check_text(text, rules):
    global rule_dict
    if not (text and rules):
        return (not text and not rules)
    r = rule_dict[rules.pop(0)]
    if type(r) == str:
        if r != text[0]:
            return False
        return check_text(text[1:], rules)
    return any(check_text(text, n_rules + rules) for n_rules in r)

rule_dict = dict(build_rules(rules))
part_1 = sum(check_text(text, ['0']) for text in texts)

rule_dict['8'] = [['42'], ['42', '8']]
rule_dict['11'] = [['42', '31'], ['42', '11', '31']]
part_2 = sum(check_text(text, ['0']) for text in texts)

print("Part 1:", part_1)
print("Part 2:", part_2)