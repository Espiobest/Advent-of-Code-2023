with open('data.txt', 'r') as r:
    lines = r.read().splitlines()

total = 0
y = 0
cardCount = {}
for i, line in enumerate(lines):
    cardCount[i] = cardCount.get(i, 0) + 1
    win, num = line.split(":")[1].split("|")
    win = [*map(int, win.split())]
    num = [*map(int, num.split())]

    x = len([card for card in num if card in win])
    if x > 0:
        total += 2**(x-1)
    for j in range(x):
        cardCount[i+j+1] = cardCount.get(i+j+1, 0) + cardCount[i]

print("Part 1:", total)
print("Part 2:", sum(cardCount.values()))
