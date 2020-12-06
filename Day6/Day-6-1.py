input_file = open("input.txt", "r").read().split('\n\n')
c = 0
for line in input_file:
    i = line.split('\n\n')
    for a in i:
        b = a.replace('\n','').split('\n')
        for d in b:
            e = "".join(set(b[0]))
            c += len(e)
print(c)

