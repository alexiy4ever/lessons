print ('Введите n: ')
n = int(input())
calc = []
for a in range(n+1):
    if a == 0 or a == 1 or n % a != 0:
        continue
    else:
        for i in range(a):
            for j in range(a):
                if i + j != a or i > j or i ==j:
                    continue
                else:
                    calc.append(i)
                    calc.append(j)
print(*calc, sep='')