# ДЗ на арифметические операции
# Частично постарался защитьтить выполнение программы
# от некорректного ввода данных(неверная операция/ нечисловое значение).
# Вся подлость в том что прошло более 2-х лет как я не писал код,
# поэтому код будет грязным и его будет много)) Постараюсь исправиться в ближайшее время. Прошу прощения.
def f(a):
    if a == 'y':
        return 1
while 1:
    print('Введите название операции: сложить"+" вычесть"-" разделить"/" умножить"*"')
    operation = input()
    if operation in ['+','-','/','*']:
        print('Введите два челых числа: ')
        num1, num2 = input(), input()
        if num1.isdigit() and num2.isdigit():
            num1, num2 = int(num1), int(num2)
        else:
            print('Введеные данные не являются числовыми. Желаете повторить? (y/n)')
            answer = input()
            if f(answer):
                continue
            else:
                print('Buy')
                break
    else:
        print('Вы ввели неверную операцию. Желаете повторить? (y/n)')
        answer = input()
        if f(answer):
            continue
        else:
            print('Buy')
            break

    if operation in ['+','-','/','*']:
        if operation == '+':
            print('Результат: ', num1+num2)
        if operation == '-':
            print('Результат: ', num1 - num2)
        if operation == '/':
            print('Результат: ', num1 / num2)
        if operation == '*':
            print('Результат: ', num1 * num2)

    else:
        print('Вы ввели неверную операцию. Желаете повторить? (y/n)')
        answer = input()
        if answer == 'y':
            continue
        else:
            print('Buy')
            break

