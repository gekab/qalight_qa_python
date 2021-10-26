def f(a, b, c):
    summa1 = 0
    summa2 = 0
    for i in range(len(a)):
        summa1 = summa1 + ord(a[i])
    for i in range(len(b)):
        summa2 = summa2 + ord(b[i])

    if a > b:
        print(summa1, '>', summa2)
        return print(c)
    if a == b:
        print(summa1, '=', summa2)
        return print('На горе стоит коза, у козы веселые глаза:)')
    else:
        print(summa1, '<', summa2)
        return print('На горе стоит коза, у козы грустные глаза:(')


f(input(), input(), input())
