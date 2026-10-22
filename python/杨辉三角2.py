rowIndex = 3
lis = []

for i in range(rowIndex+1):
    lis.append([1])
    for j in range(1, i+1):
        lis[i].append(1)
for i in range(2, len(lis)):
    for j in range(1, len(lis[i])-1):
        lis[i][j] = lis[i-1][j-1] + lis[i-1][j]
print(lis[rowIndex])













