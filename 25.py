with open('25.txt', 'r') as f:
    card_pub = int(f.readline().rstrip())
    door_pub = int(f.readline().rstrip())

def crack_loop(subject, pub_key):
    val = loop = 1
    while val != pub_key:
        val = (val*subject) % 20201227
        loop += 1
    return loop-1

# loop sizes are "private keys"
part_1 = pow(door_pub, crack_loop(7, card_pub), 20201227)

print("Part 1:", part_1)