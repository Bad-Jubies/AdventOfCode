with open('input.txt') as f:
    content = f.readlines()
c = 0
parent_bagsplit = []
for line in content:
    if "shiny gold" in line.split(' ', 3)[3]:
        parent = line.split(' ', 3)[:2]
        parent_bagsplit += parent
parents = [' '.join(x) for x in zip(parent_bagsplit[0::2], parent_bagsplit[1::2])]
c += len(parents)
print()

# index = [x for x in range(len(content)) if 'shiny gold' in content[x].lower()]
