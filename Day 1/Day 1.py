with open('data.txt', 'r') as r:
    lines = r.read().strip().split("\n\n")

part1 = 0
part2 = 0
nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for a in lines[0].split("\n"):
    digits = [s for s in a if s.isdigit()]
    first_digit = digits[0]
    last_digit = digits[-1]
    part1 += int(first_digit + last_digit)
    indexF = a.find(first_digit)
    indexL = a.rfind(last_digit)
    for i in nums:
        if a.find(i) != -1 and a.find(i) < indexF:
            first_digit, indexF = str(nums.index(i) + 1), a.find(i)
        if a.rfind(i) != -1 and a.rfind(i) > indexL:
            last_digit, indexL = str(nums.index(i) + 1), a.rfind(i)
    part2 += int(first_digit + last_digit)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
