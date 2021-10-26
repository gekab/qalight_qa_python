
def sumnum(x):
    n = 0
    for i in range(len(x)):
        n += int(x[i])
    return n

c = sumnum(input())

print('Сумма всех чисел равна:', c)