with open('18.txt', 'r') as f:
    questions = [list(l.rstrip().replace(' ', '')) for l in f.readlines()]

ops = {
    '+': lambda a, b: str(int(a)+int(b)),
    '*': lambda a, b: str(int(a)*int(b))
}

def solve(question):
    if len(question) == 1:
        return question[0]
    if question[1] == ')':
        return [question[0]] + question[2:]
    a, op, b, *question = question
    if a == '(':
        question = solve([op, b] + question)
    elif b == '(':
        question = [a, op] + solve(question)
    else:
        res = ops[op](a, b)
        question = [res] + question
    return solve(question)

# get index of matching closing bracket
def matching_bracket(question, i):
    c = 1
    while c:
        i += 1
        if question[i] == '(':
            c += 1
        elif question[i] == ')':
            c -= 1
    return i

def solve_plus(question):
    while '+' in question:
        i = question.index('+')
        a, op, b = question[i-1:i+2]
        res = ops[op](a, b)
        question = question[:i-1] + [res] + question[i+2:]
    return question

def solve2(question):
    # handle brackets first, so we can account for precedence after
    while '(' in question:
        start = question.index('(')
        end = matching_bracket(question, start)
        res = solve2(question[start+1:end])
        question = question[:start] + [res] + question[end+1:]
    # handle plus cases
    question = solve_plus(question)
    # reuse previous solve func to handle multiplication
    return solve(question)

part_1 = sum([int(x) for x in [solve(q) for q in questions]])
part_2 = sum([int(x) for x in [solve2(q) for q in questions]])

print("Part 1:", part_1)
print("Part 2:", part_2)