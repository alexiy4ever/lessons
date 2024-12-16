first = int(input ('Веедите первое число: '))
second = int(input ('Веедите второе число: '))
third = int(input ('Веедите третьее число: '))
if first == second and first == third:
    print ('3')
elif first == second or first == third or second == third:
    print ('2')
else: print ('0')