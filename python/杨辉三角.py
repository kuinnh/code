numRows = 4
yang_list = []

for i in range(numRows):
    raw = [1] * (i + 1)
    for j in range(1, i):
        raw[j] = yang_list[i-1][j-1] + yang_list[i-1][j]
    yang_list.append(raw)

print(yang_list)



