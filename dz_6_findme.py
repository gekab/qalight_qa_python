import random


def find_me(ls, xxnumber):
    if int(xxnumber) in ls:
        return [i for i in range(len(ls)) if str(ls[i]) == xxnumber]
    else:
        print('Нет такго числа в данном списке')
        exit()


l = [random.randint(0, 11) for i in range(11)]

print(l)

print('Позицию какого числа Вы ищите?: ')
x = input()
b = find_me(l, x)
print('число', x, 'находится в списке под номером:', *b)






