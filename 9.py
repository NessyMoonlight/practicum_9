n = int(input())
summ = 0

for i in range(0, n + 1):
    for j in range(0, i + 1):
        summ += (i + j)

print(summ)