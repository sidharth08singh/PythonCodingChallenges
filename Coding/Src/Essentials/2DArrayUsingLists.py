elements = []
for i in range(4):
    elements.append([])
for i in range(4):
    for j in range(4):
        elements[i].append(100)

for i in range(4):
    for j in range(4):
        print elements[i][j]
    print "\n"
