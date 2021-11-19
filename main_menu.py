#  Т.к. меню это логичиски упорядочненная структура данных, то для решения этой задачи более всего подходят списки
import  modules as m


main_menu = []
print('Меню пустое?')
print(main_menu)
actions = ['создать', 'найти', 'редактировать', 'удалить', 'выйти']
act = ''
while 1:
    print("Выбирите действие с меню:")
    print(actions)
    act = input()
    if act in actions:
        if act == actions[0]:
            print('Создаем меню:')
            while 1:
                submenu = input('Закончить создавать меню введите 0: ')
                if submenu != '0':
                    m.create_menu(main_menu, submenu)
                else:
                    break
        if act == actions[1]:
            submenu = input('Какое подменю вы ищите?: ')
            print("Запись", m.find_item_menu(main_menu, submenu), 'есть в меню')
        if act == actions[2]:
            print(main_menu)
            submenu = input('Какую запись будем менять?: ')
            nsubmenu = input('Введите новое название записи: ')
            m.edit_menu(main_menu, submenu, nsubmenu)

        if act == actions[3]:
            print(main_menu)
            submenu = input('Какую запись будем удалять?: ')
            m.del_submenu(main_menu, submenu)
        if act == actions[4]:
            m.exit_menu()
        print(main_menu)
    else:
        print('Вы не выбрали действие')

