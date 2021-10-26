'''Давайте позгнакомимся со списками?
Но не просто так, а путем генерации случайных чисел!
Необходимо написать функцию, которая будет принмать аргументы (подумайте о том, сколько их нужно!) на основаниии
которых она будет генерировать случайный список!
По умолчанию, я бы хотел, чтобы список был из натуральных числел до девятки, плюс ноль (0-9) и в длину - 10 символов.
Результат выводим в консоль.'''
import random


def f_list_gen(ls):
    return [i for i in ls]


l = [i for i in range(10)]
print(l)

print(f_list_gen((input().split())))

# можно конечно через *args, то так
print()
print('============Второй вариант решения:============')


def f_args(*args):
    return [i for i in args]


print(f_args('пн', 'вт', 'ср', 'пт', 'сб', 'вс'))
print(f_args(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))


def f_list_random(ll):
    print(ll)
    print('Минимальное число списка:')
    minn = int(input())
    print('Максимальное число списка:')
    maxx = int(input())
    return [random.randint(minn, maxx) for i in ll]

print('Список какой длины будем генерировать?:')
l = [i for i in range(int(input()))]

print(f_list_random(l))
