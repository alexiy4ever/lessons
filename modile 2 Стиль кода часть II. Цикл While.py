my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
dl = int(len(my_list))
number = 0
while True:
    if number < dl:
        if my_list[number] == 0:
            number = number + 1
            continue
        elif my_list[number] >= 0:
            print(my_list[number])
            number = number + 1
            continue
        break
    else:
        print ('Не осталось чисел')
        break
print ('Цикл завершен')

