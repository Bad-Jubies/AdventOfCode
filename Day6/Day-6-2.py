from collections import Counter

input_file = open("input.txt", "r").read().split('\n\n')
i = []
for line in input_file:
    l = line.splitlines()
    c = Counter("".join(l))
    i.append({'lines': len(l), 'count': c})

print(sum(count == a['lines'] for a in i for count in a['count'].values()))