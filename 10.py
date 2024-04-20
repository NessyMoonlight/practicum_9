n = int(input("Введите количество кубиков N<=100: "))
if n > 100:
    print('Вы ввели неверное число.')

p = [0] * (n + 1) # a list to store the number of options for each number of cubes
p[0] = 1 #base

for i in range(1, n + 1): #top row
    for j in range(1, i + 1): #bottom row
        p[i] += p[i-j] # the number of options for i cubes

print(p[n]) # number of ladders