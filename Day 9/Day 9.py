with open('data.txt', 'r') as r:
    lines = r.read().splitlines()

tot = 0
tot2 = 0
for line in lines:
    values = [*map(int, line.split())]
    history = []

    while any(values):
        arr = [j - i for i, j in zip(values, values[1:])]
        history.append(values)
        values = arr
    history.append(arr)

    prev = 0
    prev2 = 0
    for i in history[::-1][1:]:
        prev += i[-1]
        prev2 = i[0] - prev2

    tot += prev
    tot2 += prev2

print("Part 1:", tot)
print("Part 2:", tot2)
