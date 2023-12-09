import itertools
import math

with open('data.txt', 'r') as r:
    lines = r.read().splitlines()

instructions = itertools.cycle(lines[0])
mapping = {}
for line in lines[2:]:
    origin, path = line.split(" = ")
    mapping[origin] = [item.strip() for item in path[1:-1].split(',')]

steps = 0
dest = "AAA"
while dest != "ZZZ":
    steps += 1
    cur = next(instructions)

    if cur == "L":
        dest = mapping[dest][0]
    else:
        dest = mapping[dest][1]

print("Part 1:", steps)

dest = [i for i in mapping if i.endswith("A")]
all_steps = []

for i in dest:
    steps = 0
    dest = i
    while not dest.endswith("Z"):
        steps += 1
        cur = next(instructions)

        if cur == "L":
            dest = mapping[dest][0]
        else:
            dest = mapping[dest][1]

    all_steps.append(steps)

print("Part 2:", math.lcm(*all_steps))
