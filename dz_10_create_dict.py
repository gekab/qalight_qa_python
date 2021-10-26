# ДЗ 10 Словари


def create_dict(ddict, kkey, vvalue):
    ddict[kkey] = vvalue
    return ddict


d = {}
otvet = 'да'
print('===Для заполнения Базы Данных===')
while otvet == 'да':
    k, v = input('Введите Имя: '), input('Введите Фамилию: '),
    d = create_dict(d, k, v)
    otvet = input('Желаете продолжить ввод данных(да/нет) ')

print(d)
print("Печатаю БД.....")
for key, value in d.items():
    print("Имя:", key, "Фамилия:", value)
