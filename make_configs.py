import os

for i in range(1, 26):
        os.mkdir(f"Day {i}")
        template = '''with open('data.txt', 'r') as r:
        lines = r.read().strip().split("\\n\\n")'''
        open(os.path.join(f'Day {i}', f'Day {i}.py'), 'w').write(template)
        open(os.path.join(f'Day {i}', f'data.txt'), 'w').close()

print("Created folders!")
