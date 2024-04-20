n = []
k = 0
while True:
    n_ = int(input())
    if n_ == 0:
        break
    else:
        n.append(n_)
for i in range(len(n)):
    if n[i] >= 4 and n[i] % 2 == 0:
        k += 1
print(k)