import random


def f_create_list():
    l = [random.randint(0, 1001) for i in range(0, 21)]
    print(l)
    return l


lst = f_create_list()
cng = int(input())
lst[cng] = cng
print(lst)
