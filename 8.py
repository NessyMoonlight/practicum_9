x = int(input())
a = []

for i in range(1,x+1):
    for j in range(1,x+1):
        if i**2 + j**2 == x:
            a.append(i)
            a.append(j)

print(int(len(set(a)) / 2))