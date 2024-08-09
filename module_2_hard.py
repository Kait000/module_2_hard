n = int(input('Введите число: '))
sr = 0
result = ''
if n % 2 == 0:
    sr = n//2
else:
    sr = n//2+1
for i in range(1, sr):
    for j in range(i+1, n):
        if n % (i + j) == 0:
            result = result + str(i) + str(j)
print(n, '-', result)
