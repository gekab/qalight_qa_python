#  Т.к. меню это логичиски упорядочненная структура данных, то для решения этой задачи более всего подходят списки
import  modules as m


main_menu = []
while 1:
    m.create_menu(main_menu)
    answer = input("Для ПРОДОЛЖЕНИЯ создания МЕНЮ нажмите любую клавишу / для ОТМЕНЫ введите '0'")
    if answer == '0':
        break
print(main_menu)
txt = input("Какую запись в меню Вы ищете?")
print("Запись", m.find_item_menu(main_menu, txt), 'есть в меню')
txt = input("Изменить название подменю:")
txt2 = input("на новое:")
m.edit_menu(main_menu, txt, txt2)
print(main_menu)
txt = input("Удалить меню?:")
m.del_submenu(main_menu, txt)
print(main_menu)